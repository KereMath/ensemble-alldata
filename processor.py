"""
ensemble-alldata - Veri Isleme
Her binary model icin ayri dataset olustur ve tsfresh feature extraction yap.
Ornekleme: N=440 pos + 440 neg per model, her kaynak grubundan esit.
"""
import gc
import json
import random
import warnings
from pathlib import Path
from typing import Dict, List, Tuple

import numpy as np
import pandas as pd
from tqdm import tqdm
from tsfresh import extract_features as tsfresh_extract
from tsfresh.feature_extraction import EfficientFCParameters
from tsfresh.utilities.dataframe_functions import impute

from config import (
    ALL_MODEL_NAMES, MIN_SERIES_LENGTH, MODEL_POSITIVE_GROUPS, N,
    PROCESSED_DATA_DIR, RANDOM_STATE, SOURCE_GROUPS,
)

warnings.filterwarnings("ignore")
random.seed(RANDOM_STATE)

# Hizli erisim icin sozlukler
GROUP_PATHS = {gid: paths for gid, _name, paths in SOURCE_GROUPS}
GROUP_NAMES = {gid: name  for gid,  name, _paths in SOURCE_GROUPS}


# -------------------------------------------------------------------
# Yardimci: leaf klasor & CSV listeleme
# -------------------------------------------------------------------
def _get_leaf_csvs(root: Path) -> Dict[Path, List[Path]]:
    """root altindaki leaf klasorler -> CSV listesi sozlugu."""
    leaf_map: Dict[Path, List[Path]] = {}
    for f in root.rglob("*.csv"):
        if f.name == "metadata.csv":
            continue
        leaf = f.parent
        leaf_map.setdefault(leaf, []).append(f)
    return leaf_map


def sample_group(group_id: int, n: int) -> List[Path]:
    """
    Bir kaynak grubundan n CSV sec.
    Faz 1: Her leaf klasorden en az 1 sample (kapsam garantisi).
    Faz 2: Butce izin verdikce her leaften max(10, n//n_leaves) kadar topla.
    Faz 3: Hala eksikse tum havuzdan rastgele tamamla.
    Not: n < n_leaves ise shuffle+truncate ile dengeli kapsam saglanir.
    """
    leaf_map: Dict[Path, List[Path]] = {}
    for root in GROUP_PATHS[group_id]:
        if root.exists():
            for leaf, csvs in _get_leaf_csvs(root).items():
                leaf_map.setdefault(leaf, []).extend(csvs)

    if not leaf_map:
        return []

    leaves = sorted(leaf_map.keys())
    per_leaf_max = max(10, n // len(leaves))

    # Faz 1: Her leaften 1 sample al
    phase1: List[Path] = []
    leftover: Dict[Path, List[Path]] = {}
    for leaf in leaves:
        pool = sorted(leaf_map[leaf])
        if pool:
            chosen = random.choice(pool)
            phase1.append(chosen)
            leftover[leaf] = [f for f in pool if f != chosen]
        else:
            leftover[leaf] = []

    # n < n_leaves: tum leafleri kapsamak mumkun degil, shuffle+kes
    if len(phase1) >= n:
        random.shuffle(phase1)
        return phase1[:n]

    # Faz 2: Butce bittikce her leaften per_leaf_max-1 kadar daha al
    phase2: List[Path] = []
    for leaf in leaves:
        remaining_budget = n - len(phase1) - len(phase2)
        if remaining_budget <= 0:
            break
        pool = leftover[leaf]
        k = min(per_leaf_max - 1, len(pool), remaining_budget)
        if k > 0:
            phase2.extend(random.sample(pool, k))

    result = phase1 + phase2

    # Faz 3: Hala eksikse tum havuzdan tamamla
    if len(result) < n:
        all_csvs = [f for csvs in leaf_map.values() for f in csvs]
        already  = set(result)
        remaining = [f for f in all_csvs if f not in already]
        extra = min(n - len(result), len(remaining))
        if extra > 0:
            result.extend(random.sample(remaining, extra))

    random.shuffle(result)
    return result[:n]


# -------------------------------------------------------------------
# Dataset olusturma
# -------------------------------------------------------------------
def build_sample_list(model_name: str) -> Tuple[List[Path], List[int]]:
    """
    Bir binary model icin (csv_path, label) listesi dondurur.
    label: 1=pozitif, 0=negatif
    """
    pos_groups = MODEL_POSITIVE_GROUPS[model_name]
    neg_groups = set(range(1, 40)) - pos_groups

    n_pos = len(pos_groups)
    n_neg = len(neg_groups)
    pos_per_group = N // n_pos
    neg_per_group = N // n_neg

    csvs: List[Path]  = []
    labels: List[int] = []

    for gid in sorted(pos_groups):
        sampled = sample_group(gid, pos_per_group)
        csvs.extend(sampled)
        labels.extend([1] * len(sampled))

    for gid in sorted(neg_groups):
        sampled = sample_group(gid, neg_per_group)
        csvs.extend(sampled)
        labels.extend([0] * len(sampled))

    # Karistir
    combined = list(zip(csvs, labels))
    random.shuffle(combined)
    csvs_s, labels_s = zip(*combined)
    return list(csvs_s), list(labels_s)


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
# tsfresh feature extraction
# -------------------------------------------------------------------
def extract_features(series_list: List[pd.DataFrame]) -> pd.DataFrame:
    dfs = []
    for i, sdf in enumerate(series_list):
        dfs.append(pd.DataFrame({
            "id":    i,
            "time":  sdf["time"].values,
            "value": sdf["value"].values,
        }))
    combined = pd.concat(dfs, ignore_index=True)
    X_df = tsfresh_extract(
        combined,
        column_id="id",
        column_sort="time",
        column_value="value",
        default_fc_parameters=EfficientFCParameters(),
        disable_progressbar=True,
        n_jobs=4,
    )
    impute(X_df)
    return X_df


# -------------------------------------------------------------------
# Ana isleme: tek model
# -------------------------------------------------------------------
def process_model(model_name: str, force: bool = False) -> bool:
    out_dir = PROCESSED_DATA_DIR / model_name
    x_path  = out_dir / "X.npy"
    y_path  = out_dir / "y.npy"

    if not force and x_path.exists() and y_path.exists():
        X = np.load(x_path)
        y = np.load(y_path)
        print(f"  [{model_name}] Cache mevcut -> {X.shape}, pos={y.sum()}, neg={(y==0).sum()}")
        return True

    out_dir.mkdir(parents=True, exist_ok=True)

    pos_groups = MODEL_POSITIVE_GROUPS[model_name]
    neg_groups = set(range(1, 40)) - pos_groups
    print(f"\n{'='*62}")
    print(f"  MODEL: {model_name}")
    print(f"  Pozitif grup: {len(pos_groups)} ({N // len(pos_groups)}/grup)  |"
          f"  Negatif grup: {len(neg_groups)} ({N // len(neg_groups)}/grup)")
    print(f"{'='*62}")

    csvs, labels = build_sample_list(model_name)

    series_list: List[pd.DataFrame] = []
    valid_labels: List[int] = []
    failed = 0

    for csv_path, lbl in tqdm(zip(csvs, labels), total=len(csvs), desc="  CSV okuma"):
        data = read_series(csv_path)
        if len(data) < MIN_SERIES_LENGTH:
            failed += 1
            continue
        series_list.append(pd.DataFrame({
            "time":  np.arange(len(data)),
            "value": data,
        }))
        valid_labels.append(lbl)

    print(f"  Basarili: {len(series_list)}  |  Atlanan: {failed}")
    print(f"  Pozitif: {sum(valid_labels)}  |  Negatif: {len(valid_labels)-sum(valid_labels)}")

    if not series_list:
        print("  HATA: Hic ornek islenmedi!")
        return False

    print(f"  tsfresh EfficientFC ({len(series_list)} seri)...")
    X_df = extract_features(series_list)
    gc.collect()

    X = X_df.values
    y = np.array(valid_labels, dtype=int)

    np.save(x_path, X)
    np.save(y_path, y)
    with open(out_dir / "feature_names.json", "w") as f:
        json.dump(X_df.columns.tolist(), f)

    print(f"  Kaydedildi: {X.shape} -> {out_dir}")
    return True


# -------------------------------------------------------------------
# Tum modeller
# -------------------------------------------------------------------
def process_all(force: bool = False):
    print("\n" + "=" * 62)
    print("  ensemble-alldata  -  Veri Isleme (tsfresh EfficientFC)")
    print("=" * 62)
    for model_name in ALL_MODEL_NAMES:
        process_model(model_name, force=force)
    print("\nTum modeller islendi.")


if __name__ == "__main__":
    process_all()
