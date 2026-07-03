import pandas as pd
from pathlib import Path


def load_data(filepath: Path) -> pd.DataFrame:
    """Load dataset."""
    # accept either Path or string paths
    df = pd.read_csv(filepath)
    return df


def clean_data(df):
    df["column"] = df["column"].fillna(0)
    df = df[df["value"] > 0]
    return df
