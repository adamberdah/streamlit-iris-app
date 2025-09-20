import pandas as pd
from pathlib import Path

def load_data(file, use_sample: bool = False) -> pd.DataFrame:
    """Load from uploaded CSV or local sample_data/iris.csv."""
    if use_sample:
        p = Path(__file__).resolve().parents[1] / "sample_data" / "iris.csv"
        if p.exists():
            return pd.read_csv(p)
        return pd.DataFrame()  # sample not found yet
    if file is None:
        return pd.DataFrame()
    return pd.read_csv(file)