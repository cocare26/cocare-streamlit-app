import joblib
import pandas as pd


PREDICTION_MODEL_PATH = "Prediction/network_model.pkl"


try:
    prediction_model = joblib.load(PREDICTION_MODEL_PATH)
except Exception:
    prediction_model = None


REQUIRED_COLUMNS = [
    "latency",
    "packet_loss",
    "signal_strength",
    "connected_users"
]


def default_metrics():
    return {
        "latency": 0,
        "packet_loss": 0,
        "signal_strength": 0,
        "connected_users": 0
    }


def predict_network_issue(metrics: dict = None):
    if prediction_model is None:
        return 0

    if metrics is None:
        metrics = default_metrics()

    row = {col: metrics.get(col, 0) for col in REQUIRED_COLUMNS}
    X = pd.DataFrame([row])

    try:
        pred = prediction_model.predict(X)[0]
        return int(pred)
    except Exception:
        return 0
