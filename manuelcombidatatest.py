"""
Manuel Combination-Only Data Test:
Sadece kombinasyon gruplarından (grup 11-39) her leaf klasörden
en fazla SAMPLES_PER_LEAF CSV alınarak ensemble ile sınıflandırılır.
Çıktı: results/manuelcombidatatest.md
"""
import sys
import random
import warnings
from collections import defaultdict
from pathlib import Path
from typing import Dict, List, Tuple

import numpy as np
import pandas as pd
import joblib
from tsfresh import extract_features as tsfresh_extract
from tsfresh.feature_extraction import EfficientFCParameters
from tsfresh.utilities.dataframe_functions import impute

sys.path.insert(0, str(Path(__file__).parent))
from config import (
    SOURCE_GROUPS, ALL_MODEL_NAMES, BASE_MODELS, ANOMALY_MODELS,
    MODELS_DIR, RESULTS_DIR, MIN_SERIES_LENGTH, THRESHOLD, RANDOM_STATE,
)

warnings.filterwarnings("ignore")
random.seed(RANDOM_STATE)

SAMPLES_PER_LEAF = 10   # her leaf klasörden max kaç CSV alınacak

# Sadece kombinasyon grupları (11-39)
GROUP_EXPECTED = {
    11: ("deterministic_trend", ["collective_anomaly"]),
    12: ("deterministic_trend", ["mean_shift"]),
    13: ("deterministic_trend", ["point_anomaly"]),
    14: ("deterministic_trend", ["variance_shift"]),
    15: ("deterministic_trend", ["collective_anomaly"]),
    16: ("deterministic_trend", ["mean_shift"]),
    17: ("deterministic_trend", ["point_anomaly"]),
    18: ("deterministic_trend", ["variance_shift"]),
    19: ("deterministic_trend", ["collective_anomaly"]),
    20: ("deterministic_trend", ["mean_shift"]),
    21: ("deterministic_trend", ["point_anomaly"]),
    22: ("deterministic_trend", ["variance_shift"]),
    23: ("deterministic_trend", ["collective_anomaly"]),
    24: ("deterministic_trend", ["mean_shift"]),
    25: ("deterministic_trend", ["point_anomaly"]),
    26: ("deterministic_trend", ["trend_shift"]),
    27: ("deterministic_trend", ["variance_shift"]),
    28: ("deterministic_trend", ["collective_anomaly"]),
    29: ("deterministic_trend", ["mean_shift"]),
    30: ("deterministic_trend", ["point_anomaly"]),
    31: ("deterministic_trend", ["variance_shift"]),
    32: ("stochastic_trend",    ["collective_anomaly"]),
    33: ("stochastic_trend",    ["mean_shift"]),
    34: ("stochastic_trend",    ["point_anomaly"]),
    35: ("stochastic_trend",    ["variance_shift"]),
    36: ("volatility",          ["collective_anomaly"]),
    37: ("volatility",          ["mean_shift"]),
    38: ("volatility",          ["point_anomaly"]),
    39: ("volatility",          ["variance_shift"]),
}

COMBO_GROUPS = {gid for gid in GROUP_EXPECTED}


def get_leaf_csvs(root: Path) -> Dict[Path, List[Path]]:
    leaf_map: Dict[Path, List[Path]] = {}
    for f in root.rglob("*.csv"):
        if f.name == "metadata.csv":
            continue
        leaf = f.parent
        leaf_map.setdefault(leaf, []).append(f)
    return leaf_map


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


def load_models() -> Dict:
    models = {}
    for name in ALL_MODEL_NAMES:
        bundle = joblib.load(MODELS_DIR / f"{name}.pkl")
        models[name] = bundle
    return models


def predict(models: Dict, X: np.ndarray) -> Dict[str, float]:
    if X.ndim == 1:
        X = X.reshape(1, -1)
    X = np.nan_to_num(X, nan=0.0, posinf=0.0, neginf=0.0)
    probs = {}
    for name, bundle in models.items():
        X_s = bundle["scaler"].transform(X)
        probs[name] = float(bundle["model"].predict_proba(X_s)[0, 1])
    return probs


def decode(probs: Dict[str, float]) -> Tuple[str, List[str]]:
    base = max({m: probs[m] for m in BASE_MODELS}, key=lambda k: probs[k])
    anomalies = [m for m in ANOMALY_MODELS if probs[m] >= THRESHOLD]
    return base, anomalies


def match_type(true_base, true_anomalies, pred_base, pred_anomalies) -> str:
    base_ok = pred_base == true_base
    anom_ok = all(a in pred_anomalies for a in true_anomalies)
    if base_ok and anom_ok:
        return "FULL"
    elif base_ok or any(a in pred_anomalies for a in true_anomalies):
        return "PARTIAL"
    return "NONE"


def main():
    print("Modeller yükleniyor...")
    models = load_models()
    print(f"  {len(models)} model yüklendi.\n")

    all_samples = []

    print("Kombinasyon leaf klasörleri taranıyor (grup 11-39)...")
    for gid, gname, roots in SOURCE_GROUPS:
        if gid not in COMBO_GROUPS:
            continue
        true_base, true_anomalies = GROUP_EXPECTED[gid]
        for root in roots:
            if not root.exists():
                print(f"  [WARN] Bulunamadı: {root}")
                continue
            leaf_map = get_leaf_csvs(root)
            for leaf, csvs in sorted(leaf_map.items()):
                valid = [c for c in csvs if c.name != "metadata.csv"]
                if not valid:
                    continue
                k = min(SAMPLES_PER_LEAF, len(valid))
                for csv_path in random.sample(valid, k):
                    all_samples.append((gid, gname, leaf, csv_path, true_base, true_anomalies))

    print(f"  Toplam: {len(all_samples)} sample (max {SAMPLES_PER_LEAF}/leaf)\n")

    print("tsfresh feature extraction (batch)...")
    series_list = []
    valid_samples = []
    skipped = 0
    for item in all_samples:
        data = read_series(item[3])
        if len(data) >= MIN_SERIES_LENGTH:
            series_list.append(data)
            valid_samples.append(item)
        else:
            skipped += 1

    print(f"  {len(series_list)} seri extract ediliyor (atlandı: {skipped})...")
    X_all = extract_batch(series_list)
    print(f"  Tamamlandı: {X_all.shape}\n")

    print("Inference...")
    results = []
    for i, (gid, gname, leaf, csv_path, true_base, true_anomalies) in enumerate(valid_samples):
        probs = predict(models, X_all[i])
        pred_base, pred_anomalies = decode(probs)
        match = match_type(true_base, true_anomalies, pred_base, pred_anomalies)
        results.append({
            "gid": gid, "gname": gname, "leaf": leaf, "csv": csv_path,
            "true_base": true_base, "true_anomalies": true_anomalies,
            "pred_base": pred_base, "pred_anomalies": pred_anomalies,
            "probs": probs, "match": match,
        })

    total   = len(results)
    full    = sum(1 for r in results if r["match"] == "FULL")
    partial = sum(1 for r in results if r["match"] == "PARTIAL")
    none    = sum(1 for r in results if r["match"] == "NONE")
    print(f"  FULL:    {full}/{total} ({100*full/total:.1f}%)")
    print(f"  PARTIAL: {partial}/{total} ({100*partial/total:.1f}%)")
    print(f"  NONE:    {none}/{total} ({100*none/total:.1f}%)\n")

    generate_md(results, total, full, partial, none)
    print("Rapor: results/manuelcombidatatest.md")


def generate_md(results, total, full, partial, none):
    lines = []
    lines.append("# Manuel Combination-Only Data Test")
    lines.append("")
    lines.append(f"Sadece kombinasyon gruplarından (grup 11–39) her leaf klasörden")
    lines.append(f"en fazla {SAMPLES_PER_LEAF} CSV alınarak ensemble ile sınıflandırılmıştır.")
    lines.append(f"Tekli tip gruplar (1–10) bu testte yer almaz.")
    lines.append("")
    lines.append("## Özet")
    lines.append("")
    lines.append("| Metrik | Değer |")
    lines.append("|---|---|")
    lines.append(f"| Toplam test | {total} |")
    lines.append(f"| Full match | {full} ({100*full/total:.1f}%) |")
    lines.append(f"| Partial match | {partial} ({100*partial/total:.1f}%) |")
    lines.append(f"| No match | {none} ({100*none/total:.1f}%) |")
    lines.append("")

    group_stats = defaultdict(lambda: {"full": 0, "partial": 0, "none": 0, "total": 0,
                                        "gname": "", "true_base": "", "true_anom": []})
    for r in results:
        g = r["gid"]
        group_stats[g]["gname"]     = r["gname"]
        group_stats[g]["true_base"] = r["true_base"]
        group_stats[g]["true_anom"] = r["true_anomalies"]
        group_stats[g]["total"]     += 1
        group_stats[g][r["match"].lower()] += 1

    lines.append("## Grup Bazlı Özet")
    lines.append("")
    lines.append("| # | Grup | Beklenen | Örnek | Full | Partial | None | Full% |")
    lines.append("|---|---|---|---|---|---|---|---|")
    for gid in sorted(group_stats.keys()):
        s = group_stats[gid]
        expected = s["true_base"] + " + " + " + ".join(s["true_anom"])
        pct = 100 * s["full"] / s["total"] if s["total"] else 0
        lines.append(
            f"| {gid} | {s['gname']} | {expected} | {s['total']} | "
            f"{s['full']} | {s['partial']} | {s['none']} | %{pct:.0f} |"
        )
    lines.append("")

    current_gid = None
    for r in results:
        if r["gid"] != current_gid:
            current_gid = r["gid"]
            expected_str = r["true_base"] + " + " + " + ".join(r["true_anomalies"])
            lines.append("---")
            lines.append("")
            lines.append(f"## Grup {r['gid']}: {r['gname']}")
            lines.append(f"**Beklenen:** `{expected_str}`")
            lines.append("")
            lines.append("| Leaf | CSV | Tahmin | Sonuç |")
            lines.append("|---|---|---|---|")

        pred_str = r["pred_base"]
        if r["pred_anomalies"]:
            pred_str += " + " + " + ".join(sorted(r["pred_anomalies"]))
        icon = {"FULL": "✓", "PARTIAL": "~", "NONE": "✗"}[r["match"]]
        lines.append(f"| `{r['leaf'].name}` | `{r['csv'].name}` | `{pred_str}` | {icon} {r['match']} |")

    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## Model Olasılıkları — Sadece Hatalı Örnekler")
    lines.append("")
    lines.append("| Grup | CSV | stat | det | stoch | vol | coll | ctx | mean | point | trend | var | Sonuç |")
    lines.append("|---|---|---|---|---|---|---|---|---|---|---|---|---|")
    for r in results:
        if r["match"] != "FULL":
            p = r["probs"]
            lines.append(
                f"| {r['gname']} | `{r['csv'].name}` | "
                f"{p['stationary']:.2f} | {p['deterministic_trend']:.2f} | "
                f"{p['stochastic_trend']:.2f} | {p['volatility']:.2f} | "
                f"{p['collective_anomaly']:.2f} | {p['contextual_anomaly']:.2f} | "
                f"{p['mean_shift']:.2f} | {p['point_anomaly']:.2f} | "
                f"{p['trend_shift']:.2f} | {p['variance_shift']:.2f} | "
                f"{r['match']} |"
            )

    RESULTS_DIR.mkdir(exist_ok=True)
    out_path = RESULTS_DIR / "manuelcombidatatest.md"
    with open(out_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))


if __name__ == "__main__":
    main()
