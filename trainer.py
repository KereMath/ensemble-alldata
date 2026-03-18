"""
ensemble-alldata - Binary Model Egitimi
Her anomali/base tipi icin ayri binary classifier.
LightGBM + XGBoost + MLP — en iyi val F1 seçilir.
Inference: base_type=argmax, anomalies=threshold(>=0.5)
"""
import json
import warnings
from pathlib import Path
from typing import Any, Dict

import joblib
import numpy as np
from sklearn.metrics import accuracy_score, classification_report, f1_score
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler
import lightgbm as lgb
import xgboost as xgb

from config import (
    ALL_MODEL_NAMES, BASE_MODELS, ANOMALY_MODELS,
    MODELS_DIR, PROCESSED_DATA_DIR, RANDOM_STATE,
    RESULTS_DIR, TEST_SIZE, THRESHOLD, VALIDATION_SIZE,
)

warnings.filterwarnings("ignore")


# -------------------------------------------------------------------
# Veri yukleme
# -------------------------------------------------------------------
def load_model_data(model_name: str):
    d = PROCESSED_DATA_DIR / model_name
    X = np.load(d / "X.npy")
    y = np.load(d / "y.npy")
    return X, y


# -------------------------------------------------------------------
# Classifier tarifler
# -------------------------------------------------------------------
def build_classifiers(pos_weight: float) -> Dict[str, Any]:
    return {
        "LightGBM": lgb.LGBMClassifier(
            n_estimators=300, learning_rate=0.05, max_depth=7,
            num_leaves=63, subsample=0.8, colsample_bytree=0.8,
            class_weight="balanced",
            random_state=RANDOM_STATE, n_jobs=-1, verbose=-1,
        ),
        "XGBoost": xgb.XGBClassifier(
            n_estimators=300, learning_rate=0.05, max_depth=7,
            subsample=0.8, colsample_bytree=0.8,
            scale_pos_weight=pos_weight,
            random_state=RANDOM_STATE, n_jobs=-1,
            eval_metric="logloss", verbosity=0,
        ),
        "MLP": MLPClassifier(
            hidden_layer_sizes=(256, 128, 64), max_iter=500,
            early_stopping=True, validation_fraction=0.1,
            random_state=RANDOM_STATE,
        ),
    }


# -------------------------------------------------------------------
# Tek model egitimi
# -------------------------------------------------------------------
def train_binary_model(model_name: str) -> Dict[str, Any]:
    print(f"\n{'='*62}")
    print(f"  BINARY MODEL: {model_name}")
    print(f"{'='*62}")

    X, y = load_model_data(model_name)
    X = np.nan_to_num(X, nan=0.0, posinf=0.0, neginf=0.0)
    print(f"  Veri: {X.shape}  |  Pos: {y.sum()}  |  Neg: {(y==0).sum()}")

    # Train / Val / Test bolme
    val_ratio_adj = VALIDATION_SIZE / (1 - TEST_SIZE)
    X_tmp, X_te, y_tmp, y_te = train_test_split(
        X, y, test_size=TEST_SIZE, random_state=RANDOM_STATE, stratify=y,
    )
    X_tr, X_val, y_tr, y_val = train_test_split(
        X_tmp, y_tmp, test_size=val_ratio_adj, random_state=RANDOM_STATE, stratify=y_tmp,
    )
    print(f"  Train: {len(X_tr)}  |  Val: {len(X_val)}  |  Test: {len(X_te)}")

    # Olcekleme
    scaler  = StandardScaler()
    X_tr_s  = scaler.fit_transform(X_tr)
    X_val_s = scaler.transform(X_val)
    X_te_s  = scaler.transform(X_te)

    # XGBoost pos_weight
    pos_count  = int(y_tr.sum())
    neg_count  = int(len(y_tr) - pos_count)
    pos_weight = neg_count / pos_count if pos_count > 0 else 1.0

    classifiers = build_classifiers(pos_weight)
    val_scores: Dict[str, Any] = {}

    for clf_name, clf in classifiers.items():
        clf.fit(X_tr_s, y_tr)
        pred_val = clf.predict(X_val_s)
        f1  = f1_score(y_val, pred_val, average="binary", zero_division=0)
        acc = accuracy_score(y_val, pred_val)
        val_scores[clf_name] = {"f1": f1, "acc": acc, "model": clf}
        print(f"  {clf_name:<12}  Val F1={f1:.4f}  Acc={acc:.4f}")

    best_name  = max(val_scores, key=lambda k: val_scores[k]["f1"])
    best_model = val_scores[best_name]["model"]

    pred_te = best_model.predict(X_te_s)
    test_f1  = f1_score(y_te, pred_te, average="binary", zero_division=0)
    test_acc = accuracy_score(y_te, pred_te)

    print(f"\n  >>> En iyi: {best_name}  |  Test F1={test_f1:.4f}  Acc={test_acc:.4f}")
    print(classification_report(
        y_te, pred_te, target_names=["negatif", "pozitif"], digits=4, zero_division=0,
    ))

    # Modeli kaydet
    MODELS_DIR.mkdir(exist_ok=True)
    model_path = MODELS_DIR / f"{model_name}.pkl"
    joblib.dump({"model": best_model, "scaler": scaler}, model_path)
    print(f"  Model kaydedildi: {model_path}")

    return {
        "best_clf":   best_name,
        "test_f1":    round(float(test_f1),  4),
        "test_acc":   round(float(test_acc), 4),
        "val_scores": {
            k: {"f1": round(float(v["f1"]), 4), "acc": round(float(v["acc"]), 4)}
            for k, v in val_scores.items()
        },
        "pos_count":  int(y.sum()),
        "neg_count":  int((y == 0).sum()),
        "n_features": int(X.shape[1]),
    }


# -------------------------------------------------------------------
# Tum modeller
# -------------------------------------------------------------------
def train_all() -> Dict[str, Any]:
    print("\n" + "=" * 62)
    print("  ensemble-alldata  -  Model Egitimi (10 Binary Classifier)")
    print("=" * 62)

    results = {}
    for model_name in ALL_MODEL_NAMES:
        results[model_name] = train_binary_model(model_name)

    # Ozet tablo
    print("\n" + "=" * 62)
    print("  OZET")
    print("=" * 62)
    print(f"  {'Model':<25}  {'En iyi':<10}  {'Test F1':>8}  {'Test Acc':>9}")
    print(f"  {'-'*25}  {'-'*10}  {'-'*8}  {'-'*9}")
    for name, res in results.items():
        tag = " [BASE]" if name in BASE_MODELS else ""
        print(f"  {name+tag:<25}  {res['best_clf']:<10}  "
              f"{res['test_f1']:>8.4f}  {res['test_acc']:>9.4f}")

    RESULTS_DIR.mkdir(exist_ok=True)
    out = RESULTS_DIR / "training_results.json"
    with open(out, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
    print(f"\nSonuclar: {out}")

    return results


if __name__ == "__main__":
    train_all()
