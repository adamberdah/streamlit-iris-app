import pandas as pd
from app.viz import quick_plot

def test_quick_plot_returns_figure():
    df = pd.DataFrame({"x": [1, 2, 3], "y": [4, 5, 6]})
    fig = quick_plot(df, "x", "y")
    assert hasattr(fig, "axes")
    assert len(fig.axes) == 1
