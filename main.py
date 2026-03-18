"""
ensemble-alldata - Ana Calistirma Scripti

Kullanim:
    python main.py                      # isleme + egitim + kombinasyon testi
    python main.py --force              # cache'i yoksay, bastan isle
    python main.py --train              # sadece egitim (isleme atlandi)
    python main.py --eval               # sadece kombinasyon testi (modeller hazir olmali)
    python main.py --model mean_shift   # tek model icin isleme + egitim
"""
import sys
from pathlib import Path

from config import ALL_MODEL_NAMES, PROCESSED_DATA_DIR


def cache_exists(model_name: str) -> bool:
    d = PROCESSED_DATA_DIR / model_name
    return (d / "X.npy").exists() and (d / "y.npy").exists()


def main():
    force      = "--force" in sys.argv
    train_only = "--train" in sys.argv
    eval_only  = "--eval"  in sys.argv

    single_model = None
    if "--model" in sys.argv:
        idx = sys.argv.index("--model")
        if idx + 1 < len(sys.argv):
            single_model = sys.argv[idx + 1]
            if single_model not in ALL_MODEL_NAMES:
                print(f"Gecersiz model: {single_model}")
                print(f"Gecerli modeller: {ALL_MODEL_NAMES}")
                sys.exit(1)

    targets = [single_model] if single_model else ALL_MODEL_NAMES

    print("=" * 62)
    print("  ensemble-alldata  —  Binary Ensemble Egitimi")
    print(f"  N=440 pos + 440 neg per model  |  10 binary classifier")
    print("=" * 62)
    print(f"  Hedef modeller: {targets}")

    # ------------------------------------------------------------------
    # Adim 1: Feature extraction (processor)
    # ------------------------------------------------------------------
    if not train_only and not eval_only:
        from processor import process_model
        print("\n>> Adim 1/3: Feature extraction (tsfresh EfficientFC)")
        for model_name in targets:
            if force or not cache_exists(model_name):
                process_model(model_name, force=force)
            else:
                import numpy as np
                X = np.load(PROCESSED_DATA_DIR / model_name / "X.npy")
                y = np.load(PROCESSED_DATA_DIR / model_name / "y.npy")
                print(f"  [{model_name}] Cache bulundu -> {X.shape}, "
                      f"pos={int(y.sum())}, neg={int((y==0).sum())}")
    else:
        print("\n>> Adim 1/3: Feature extraction atlandi.")

    # ------------------------------------------------------------------
    # Adim 2: Egitim (trainer)
    # ------------------------------------------------------------------
    if not eval_only:
        from trainer import train_binary_model, train_all
        import json
        from config import RESULTS_DIR

        print("\n>> Adim 2/3: Binary model egitimi")
        if single_model:
            result = {single_model: train_binary_model(single_model)}
        else:
            result = train_all()
    else:
        print("\n>> Adim 2/3: Egitim atlandi.")

    # ------------------------------------------------------------------
    # Adim 3: Kombinasyon degerlendirmesi (evaluator)
    # ------------------------------------------------------------------
    if not single_model or "--eval" in sys.argv:
        from evaluator import load_all_models, evaluate_combinations
        print("\n>> Adim 3/3: Kombinasyon testi")
        models = load_all_models()
        evaluate_combinations(models)
    else:
        print(f"\n>> Adim 3/3: Tek model modu — kombinasyon testi atlandi.")
        print("   Tum modeller egitilince: python main.py --eval")

    print("\nTamamlandi.")


if __name__ == "__main__":
    main()
