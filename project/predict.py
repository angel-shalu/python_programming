import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression


def predict_stock(csv_path="stock_log.csv", days_ahead=7):
    """Train a simple linear regression on historical daily stock and predict future stock."""
    try:
        df = pd.read_csv(csv_path, parse_dates=["date"]) 
    except Exception:
        return None, "no-data"

    if len(df) < 2:
        return None, "not-enough-data"

    df = df.sort_values("date").reset_index(drop=True)
    df["day"] = np.arange(len(df))
    X = df[["day"]]
    y = df["stock"]

    model = LinearRegression()
    model.fit(X, y)
    future_day = np.array([[len(df) + days_ahead - 1]])
    pred = model.predict(future_day)[0]
    score = model.score(X, y)
    return float(pred), float(score)
