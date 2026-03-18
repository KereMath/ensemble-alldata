"""
ensemble-alldata - Konfigurasyon
10 binary classifier: 4 base tip + 6 anomali tipi
Her model: 440 pozitif + 440 negatif ornek (esit grup temsili)
"""
from pathlib import Path

BASE_DIR           = Path(__file__).parent
GD                 = Path(r"C:\Users\user\Desktop\Generated Data")
COMB               = GD / "Combinations"

PROCESSED_DATA_DIR = BASE_DIR / "processed_data"
MODELS_DIR         = BASE_DIR / "trained_models"
RESULTS_DIR        = BASE_DIR / "results"

N                  = 1320       # pozitif ve negatif ornek sayisi (per model)
MIN_SERIES_LENGTH  = 50
RANDOM_STATE       = 42
TEST_SIZE          = 0.20
VALIDATION_SIZE    = 0.10
THRESHOLD          = 0.5        # anomali modelleri icin pozitif esik

# -------------------------------------------------------------------
# 39 Kaynak Grubu: (id, name, [root_paths])
# -------------------------------------------------------------------
SOURCE_GROUPS = [
    # --- Tekli tipler (1-10) ---
    (1,  "stationary",           [GD / "stationary"]),
    (2,  "deterministic_trend",  [GD / "deterministic_trend"]),
    (3,  "stochastic_trend",     [GD / "Stochastic Trend"]),
    (4,  "volatility",           [GD / "Volatility"]),
    (5,  "collective_anomaly",   [GD / "collective_anomaly"]),
    (6,  "contextual_anomaly",   [GD / "contextual_anomaly"]),
    (7,  "mean_shift",           [GD / "mean_shift"]),
    (8,  "point_anomaly",        [GD / "point_anomaly"]),
    (9,  "trend_shift",          [GD / "trend_shift"]),
    (10, "variance_shift",       [GD / "variance_shift"]),
    # --- Cubic Base kombinasyonlari (11-14) ---
    (11, "cubic+collective",     [COMB / "Cubic Base" / "Cubic Base" / "cubic_collective_anomaly"]),
    (12, "cubic+mean_shift",     [COMB / "Cubic Base" / "Cubic Base" / "Cubic + Mean Shift"]),
    (13, "cubic+point_anomaly",  [COMB / "Cubic Base" / "Cubic Base" / "Cubic + Point Anomaly"]),
    (14, "cubic+variance_shift", [COMB / "Cubic Base" / "Cubic Base" / "Cubic + Variance Shift"]),
    # --- Damped Base kombinasyonlari (15-18) ---
    (15, "damped+collective",    [COMB / "Damped Base" / "Damped Base" / "Damped + Collective Anomaly"]),
    (16, "damped+mean_shift",    [COMB / "Damped Base" / "Damped Base" / "Damped + Mean Shift"]),
    (17, "damped+point_anomaly", [COMB / "Damped Base" / "Damped Base" / "Damped + Point Anomaly"]),
    (18, "damped+variance_shift",[COMB / "Damped Base" / "Damped Base" / "Damped + Variance Shift"]),
    # --- Exponential Base kombinasyonlari (19-22) ---
    (19, "exp+collective",       [COMB / "Exponential Base" / "Exponential Base" / "exponential_collective_anomaly"]),
    (20, "exp+mean_shift",       [COMB / "Exponential Base" / "Exponential Base" / "Exponential + Mean Shift"]),
    (21, "exp+point_anomaly",    [COMB / "Exponential Base" / "Exponential Base" / "exponential_point_anomaly"]),
    (22, "exp+variance_shift",   [COMB / "Exponential Base" / "Exponential Base" / "exponential_variance_shift"]),
    # --- Linear Base kombinasyonlari (23-27) ---
    (23, "linear+collective",    [COMB / "Linear Base" / "Linear Base" / "Linear + Collective Anomaly"]),
    (24, "linear+mean_shift",    [COMB / "Linear Base" / "Linear Base" / "Linear + Mean Shift"]),
    (25, "linear+point_anomaly", [COMB / "Linear Base" / "Linear Base" / "Linear + Point Anomaly"]),
    (26, "linear+trend_shift",   [COMB / "Linear Base" / "Linear Base" / "Linear + Trend Shift"]),
    (27, "linear+variance_shift",[COMB / "Linear Base" / "Linear Base" / "Linear + Variance Shift"]),
    # --- Quadratic Base kombinasyonlari (28-31) ---
    (28, "quad+collective",      [COMB / "Quadratic Base" / "Quadratic Base" / "Quadratic + Collective anomaly"]),
    (29, "quad+mean_shift",      [COMB / "Quadratic Base" / "Quadratic Base" / "Quadratic + Mean Shift"]),
    (30, "quad+point_anomaly",   [COMB / "Quadratic Base" / "Quadratic Base" / "Quadratic + Point Anomaly"]),
    (31, "quad+variance_shift",  [COMB / "Quadratic Base" / "Quadratic Base" / "Quadratic + Variance Shift"]),
    # --- Stochastic Trend kombinasyonlari (32-35) ---
    (32, "stoch+collective",     [COMB / "Stochastic Trend + Collective Anomaly"]),
    (33, "stoch+mean_shift",     [COMB / "Stochastic Trend + Mean Shift"]),
    (34, "stoch+point_anomaly",  [COMB / "Stochastic Trend + Point Anomaly"]),
    (35, "stoch+variance_shift", [COMB / "Stochastic Trend + Variance Shift" / "Stochastic Trend + Variance Shift"]),
    # --- Volatility kombinasyonlari (36-39) ---
    (36, "vol+collective",       [COMB / "Volatility + Collective Anomaly"]),
    (37, "vol+mean_shift",       [COMB / "Volatility + Mean Shift"]),
    (38, "vol+point_anomaly",    [COMB / "Volatility + Point Anomaly"]),
    (39, "vol+variance_shift",   [COMB / "Volatility + Variance Shift"]),
]

# -------------------------------------------------------------------
# Her modelin pozitif kaynak grubu ID'leri
# -------------------------------------------------------------------
MODEL_POSITIVE_GROUPS = {
    "stationary":          {1, 5, 6, 7, 8, 9, 10},
    "deterministic_trend": {2, 11, 12, 13, 14, 15, 16, 17, 18,
                             19, 20, 21, 22, 23, 24, 25, 26, 27,
                             28, 29, 30, 31},
    "stochastic_trend":    {3, 32, 33, 34, 35},
    "volatility":          {4, 36, 37, 38, 39},
    "collective_anomaly":  {5, 11, 15, 19, 23, 28, 32, 36},
    "contextual_anomaly":  {6},
    "mean_shift":          {7, 12, 16, 20, 24, 29, 33, 37},
    "point_anomaly":       {8, 13, 17, 21, 25, 30, 34, 38},
    "trend_shift":         {9, 26},
    "variance_shift":      {10, 14, 18, 22, 27, 31, 35, 39},
}

ALL_MODEL_NAMES = [
    "stationary", "deterministic_trend", "stochastic_trend", "volatility",
    "collective_anomaly", "contextual_anomaly", "mean_shift",
    "point_anomaly", "trend_shift", "variance_shift",
]

BASE_MODELS    = ["stationary", "deterministic_trend", "stochastic_trend", "volatility"]
ANOMALY_MODELS = ["collective_anomaly", "contextual_anomaly", "mean_shift",
                  "point_anomaly", "trend_shift", "variance_shift"]
