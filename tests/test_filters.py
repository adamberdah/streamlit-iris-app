import pandas as pd
from app.filters import apply_filters

def test_apply_filters_columns_and_min_rows():
    df = pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
    out = apply_filters(df, columns=["a"], min_rows=2)
    assert list(out.columns) == ["a"]
    assert len(out) == 3

def test_apply_filters_min_rows_enforced_to_empty():
    df = pd.DataFrame({"a": [1, 2, 3]})
    out = apply_filters(df, columns=["a"], min_rows=5)
    assert out.empty
