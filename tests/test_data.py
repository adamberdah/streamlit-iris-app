import pandas as pd
from app.data import load_data

def test_sample_load_not_empty():
    df = load_data(file=None, use_sample=True)
    assert isinstance(df, pd.DataFrame)
    assert not df.empty
    assert "target" in df.columns