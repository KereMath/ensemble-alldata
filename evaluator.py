"""
ensemble-alldata - Kombinasyon Degerlendirmesi
Eski tsfresh ensemble ile karsilastirmali test:
  - Tum Combinations klasoru uzerinde full/partial/no-match
  - Her kombinasyon tipi icin ayri breakown
  - Sonuclar results/combination_eval.json'a kaydedilir
"""
import json
import warnings
from collections import defaultdict
from pathlib import Path
from typing import Any, Dict, List, Tuple

import joblib
import numpy as np
import pandas as pd
from tqdm import tqdm
from tsfresh import extract_features as tsfresh_extract
from tsfresh.feature_extraction import EfficientFCParameters
from tsfresh.utilities.dataframe_functions import impute

from config import (
    ALL_MODEL_NAMES, ANOMALY_MODELS, BASE_MODELS, COMB, GD,
    MIN_SERIES_LENGTH, MODELS_DIR, RANDOM_STATE, RESULTS_DIR, THRESHOLD,
)

warnings.filterwarnings("ignore")

# -------------------------------------------------------------------
# Kombinasyon testi icin ground-truth tanimi
# Eski tsfresh ensemble'dan aynen alinmistir (true_labels konvansiyonu)
# -------------------------------------------------------------------
COMBINATION_LABELS = [
    # (klasor_yolu_parca_listesi, [base_label, anomaly_label])
    (["Cubic Base", "Cubic Base", "cubic_collective_anomaly"],      ["deterministic_trend", "collective_anomaly"]),
    (["Cubic Base", "Cubic Base", "Cubic + Mean Shift"],            ["deterministic_trend", "mean_shift"]),
    (["Cubic Base", "Cubic Base", "Cubic + Point Anomaly"],         ["deterministic_trend", "point_anomaly"]),
    (["Cubic Base", "Cubic Base", "Cubic + Variance Shift"],        ["deterministic_trend", "variance_shift"]),
    (["Damped Base", "Damped Base", "Damped + Collective Anomaly"], ["deterministic_trend", "collective_anomaly"]),
    (["Damped Base", "Damped Base", "Damped + Mean Shift"],         ["deterministic_trend", "mean_shift"]),
    (["Damped Base", "Damped Base", "Damped + Point Anomaly"],      ["deterministic_trend", "point_anomaly"]),
    (["Damped Base", "Damped Base", "Damped + Variance Shift"],     ["deterministic_trend", "variance_shift"]),
    (["Exponential Base", "Exponential Base", "exponential_collective_anomaly"], ["deterministic_trend", "collective_anomaly"]),
    (["Exponential Base", "Exponential Base", "Exponential + Mean Shift"],       ["deterministic_trend", "mean_shift"]),
    (["Exponential Base", "Exponential Base", "exponential_point_anomaly"],      ["deterministic_trend", "point_anomaly"]),
    (["Exponential Base", "Exponential Base", "exponential_variance_shift"],     ["deterministic_trend", "variance_shift"]),
    (["Linear Base", "Linear Base", "Linear + Collective Anomaly"], ["deterministic_trend", "collective_anomaly"]),
    (["Linear Base", "Linear Base", "Linear + Mean Shift"],         ["deterministic_trend", "mean_shift"]),
    (["Linear Base", "Linear Base", "Linear + Point Anomaly"],      ["deterministic_trend", "point_anomaly"]),
    (["Linear Base", "Linear Base", "Linear + Trend Shift"],        ["deterministic_trend", "trend_shift"]),
    (["Linear Base", "Linear Base", "Linear + Variance Shift"],     ["deterministic_trend", "variance_shift"]),
    (["Quadratic Base", "Quadratic Base", "Quadratic + Collective anomaly"], ["deterministic_trend", "collective_anomaly"]),
    (["Quadratic Base", "Quadratic Base", "Quadratic + Mean Shift"],         ["deterministic_trend", "mean_shift"]),
    (["Quadratic Base", "Quadratic Base", "Quadratic + Point Anomaly"],      ["deterministic_trend", "point_anomaly"]),
    (["Quadratic Base", "Quadratic Base", "Quadratic + Variance Shift"],     ["deterministic_trend", "variance_shift"]),
    (["Stochastic Trend + Collective Anomaly"],                      ["stochastic_trend", "collective_anomaly"]),
    (["Stochastic Trend + Mean Shift"],                              ["stochastic_trend", "mean_shift"]),
    (["Stochastic Trend + Point Anomaly"],                           ["stochastic_trend", "point_anomaly"]),
    (["Stochastic Trend + Variance Shift", "Stochastic Trend + Variance Shift"], ["stochastic_trend", "variance_shift"]),
    (["Volatility + Collective Anomaly"],                            ["volatility", "collective_anomaly"]),
    (["Volatility + Mean Shift"],                                    ["volatility", "mean_shift"]),
    (["Volatility + Point Anomaly"],                                 ["volatility", "point_anomaly"]),
    (["Volatility + Variance Shift"],                                ["volatility", "variance_shift"]),
]

SAMPLES_PER_COMBO = 10   # her kombinasyon klasoründen kac CSV test edilecek


# -------------------------------------------------------------------
# CSV okuma
# -------------------------------------------------------------------
def read_series(csv_path: Path) -> np.ndarray:
    try:
        df = pd.read_csv(csv_path)
        for col in ("data", "value", "values", "y"):
            if col in df.columns:
                return df[col].dropna().values.astype(float)
        num_cols = df.select_dtypes(include=[float, int]).columns
        if len(num_cols) > 0:
            return df[num_cols[0]].dropna().values.astype(float)
    except Exception:
        pass
    return np.array([])


# -------------------------------------------------------------------
# tsfresh
# -------------------------------------------------------------------
def extract_single(series: np.ndarray) -> np.ndarray:
    df = pd.DataFrame({"id": 0, "time": np.arange(len(series)), "value": series})
    X_df = tsfresh_extract(
        df,
        column_id="id", column_sort="time", column_value="value",
        default_fc_parameters=EfficientFCParameters(),
        disable_progressbar=True, n_jobs=1,
    )
    impute(X_df)
    return X_df.values[0]


def extract_batch(series_list: List[np.ndarray]) -> np.ndarray:
    dfs = []
    for i, s in enumerate(series_list):
        dfs.append(pd.DataFrame({"id": i, "time": np.arange(len(s)), "value": s}))
    combined = pd.concat(dfs, ignore_index=True)
    X_df = tsfresh_extract(
        combined,
        column_id="id", column_sort="time", column_value="value",
        default_fc_parameters=EfficientFCParameters(),
        disable_progressbar=True, n_jobs=4,
    )
    impute(X_df)
    return X_df.values


# -------------------------------------------------------------------
# Model yukleme ve inference
# -------------------------------------------------------------------
def load_all_models() -> Dict[str, Any]:
    models = {}
    for name in ALL_MODEL_NAMES:
        path = MODELS_DIR / f"{name}.pkl"
        if not path.exists():
            raise FileNotFoundError(f"Model bulunamadi: {path}  (once main.py calistirin)")
        bundle = joblib.load(path)
        models[name] = bundle
    print(f"  {len(models)} model yuklendi.")
    return models


def predict(models: Dict[str, Any], X_features: np.ndarray) -> Dict[str, float]:
    """
    X_features: (1, n_features) veya (n_features,)
    Returns: {model_name: P(pozitif)}
    """
    if X_features.ndim == 1:
        X_features = X_features.reshape(1, -1)
    X_clean = np.nan_to_num(X_features, nan=0.0, posinf=0.0, neginf=0.0)
    probs = {}
    for name, bundle in models.items():
        X_scaled = bundle["scaler"].transform(X_clean)
        prob = bundle["model"].predict_proba(X_scaled)[0, 1]
        probs[name] = float(prob)
    return probs


def decode_prediction(probs: Dict[str, float]) -> Tuple[str, List[str]]:
    """
    base_type  = argmax(4 base model)
    anomalies  = [model for anomaly_models if prob >= THRESHOLD]
    """
    base_probs = {m: probs[m] for m in BASE_MODELS}
    base_type  = max(base_probs, key=base_probs.get)

    anomalies = [m for m in ANOMALY_MODELS if probs[m] >= THRESHOLD]
    return base_type, anomalies


# -------------------------------------------------------------------
# Kombinasyon testi
# -------------------------------------------------------------------
def evaluate_combinations(models: Dict[str, Any]) -> Dict[str, Any]:
    print("\n" + "=" * 62)
    print("  Kombinasyon Testi")
    print("=" * 62)

    all_results = []

    for path_parts, true_labels in COMBINATION_LABELS:
        combo_dir = COMB
        for part in path_parts:
            combo_dir = combo_dir / part

        if not combo_dir.exists():
            print(f"  [WARN] Bulunamadi: {combo_dir}")
            continue

        # CSV'leri topla
        csvs = sorted([
            f for f in combo_dir.rglob("*.csv")
            if f.name != "metadata.csv"
        ])
        if not csvs:
            continue

        import random
        random.seed(RANDOM_STATE)
        sample_csvs = random.sample(csvs, min(SAMPLES_PER_COMBO, len(csvs)))

        combo_name = " + ".join(path_parts[-1:])
        print(f"  {combo_name[:55]:<55}  ({len(sample_csvs)} CSV)")

        # Batch feature extraction
        series_list = []
        valid_csvs  = []
        for csv_path in sample_csvs:
            data = read_series(csv_path)
            if len(data) >= MIN_SERIES_LENGTH:
                series_list.append(data)
                valid_csvs.append(csv_path)

        if not series_list:
            continue

        X_batch = extract_batch(series_list)

        true_base    = true_labels[0]
        true_anomaly = true_labels[1]

        for i, csv_path in enumerate(valid_csvs):
            probs = predict(models, X_batch[i])
            pred_base, pred_anomalies = decode_prediction(probs)

            base_correct    = (pred_base == true_base)
            anomaly_correct = (true_anomaly in pred_anomalies)
            full_match      = base_correct and anomaly_correct
            partial_match   = base_correct or anomaly_correct
            no_match        = not partial_match

            all_results.append({
                "combo":          combo_name,
                "true_base":      true_base,
                "true_anomaly":   true_anomaly,
                "pred_base":      pred_base,
                "pred_anomalies": pred_anomalies,
                "probs":          {k: round(v, 4) for k, v in probs.items()},
                "base_correct":   base_correct,
                "anomaly_correct":anomaly_correct,
                "full_match":     full_match,
                "partial_match":  partial_match and not full_match,
                "no_match":       no_match,
            })

    # Istatistik
    total        = len(all_results)
    full_match   = sum(1 for r in all_results if r["full_match"])
    partial_match= sum(1 for r in all_results if r["partial_match"])
    no_match     = sum(1 for r in all_results if r["no_match"])

    print(f"\n{'='*62}")
    print(f"  TOPLAM: {total} test")
    print(f"  Full match  (ikisini de buldu) : {full_match:4d}  ({100*full_match/total:.1f}%)")
    print(f"  Partial     (birini buldu)     : {partial_match:4d}  ({100*partial_match/total:.1f}%)")
    print(f"  No match    (hic bulamadi)     : {no_match:4d}  ({100*no_match/total:.1f}%)")

    # Per-combo breakdown
    combo_stats = defaultdict(lambda: {"total": 0, "full": 0, "partial": 0, "none": 0})
    for r in all_results:
        c = r["combo"]
        combo_stats[c]["total"] += 1
        if r["full_match"]:    combo_stats[c]["full"]    += 1
        elif r["partial_match"]:combo_stats[c]["partial"] += 1
        else:                   combo_stats[c]["none"]    += 1

    print(f"\n  {'Kombinasyon':<45}  {'Full':>5}  {'Part':>5}  {'None':>5}")
    print(f"  {'-'*45}  {'-'*5}  {'-'*5}  {'-'*5}")
    for combo, s in sorted(combo_stats.items()):
        rate = 100 * s["full"] / s["total"]
        print(f"  {combo[:45]:<45}  {s['full']:3d}/{s['total']}  {s['partial']:5d}  {s['none']:5d}  ({rate:.0f}%)")

    out = {
        "total":         total,
        "full_match":    full_match,
        "full_match_pct":round(100 * full_match / total, 2) if total else 0,
        "partial_match": partial_match,
        "no_match":      no_match,
        "per_combo":     {
            k: {"full": v["full"], "partial": v["partial"], "none": v["none"],
                "total": v["total"], "rate": round(100*v["full"]/v["total"], 1)}
            for k, v in combo_stats.items()
        },
        "per_sample":    all_results,
    }

    RESULTS_DIR.mkdir(exist_ok=True)
    out_path = RESULTS_DIR / "combination_eval.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2, ensure_ascii=False)
    print(f"\n  Sonuclar: {out_path}")

    return out


# -------------------------------------------------------------------
# Tek sinyal inference (disa acik API)
# -------------------------------------------------------------------
def predict_csv(csv_path: Path, models: Dict[str, Any]) -> Dict[str, Any]:
    data = read_series(csv_path)
    if len(data) < MIN_SERIES_LENGTH:
        return {"error": "seri cok kisa"}
    features = extract_single(data)
    probs     = predict(models, features)
    base, anomalies = decode_prediction(probs)
    return {
        "base_type": base,
        "anomalies": anomalies,
        "probs":     {k: round(v, 4) for k, v in probs.items()},
    }


if __name__ == "__main__":
    models = load_all_models()
    evaluate_combinations(models)
