import joblib
import pandas as pd

PREDICTION_MODEL_PATH = "Prediction/network_model.pkl"

try:
    prediction_model = joblib.load(PREDICTION_MODEL_PATH)
except Exception:
    prediction_model = None


def predict_network_issue(metrics: dict):
    if prediction_model is None or not metrics:
        return None

    required_columns = ["latency", "packet_loss", "signal_strength", "connected_users"]

    row = {col: metrics.get(col, 0) for col in required_columns}
    X = pd.DataFrame([row])

    try:
        pred = prediction_model.predict(X)[0]
        return int(pred) if str(pred).isdigit() else pred
    except Exception:
        return None