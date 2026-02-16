import pandas as pd
from datetime import datetime


def append_stock(count, csv_path="stock_log.csv"):
    """Append a single stock row (UTC ISO date, stock) to CSV."""
    df = pd.DataFrame([[datetime.utcnow().isoformat(), int(count)]], columns=["date", "stock"])
    try:
        # if file exists, don't write header
        with open(csv_path, "r"):
            header = False
    except FileNotFoundError:
        header = True
    df.to_csv(csv_path, mode="a", header=header, index=False)


def load_stock(csv_path="stock_log.csv"):
    try:
        df = pd.read_csv(csv_path, parse_dates=["date"]) 
        return df
    except Exception:
        return pd.DataFrame(columns=["date", "stock"]) 
