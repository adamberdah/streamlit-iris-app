import pandas as pd

def apply_filters(df: pd.DataFrame, columns=None, min_rows: int = 0) -> pd.DataFrame:
    if df is None or df.empty:
        return df
    if columns:
        df = df[columns]
    if len(df) < min_rows:
        return df.iloc[0:0]  # enforce rule by returning empty
    return df
