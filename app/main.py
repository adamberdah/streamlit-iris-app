# --- bootstrap sys.path so 'app' package is importable ---
import os, sys
ROOT = os.path.dirname(os.path.dirname(__file__))  # project root
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)
# ---------------------------------------------------------

import streamlit as st
import pandas as pd
from app.data import load_data
from app.filters import apply_filters
from app.viz import quick_plot

st.set_page_config(page_title="Iris Explorer", page_icon="🌸", layout="wide")
st.title("Iris Explorer")

with st.sidebar:
    st.header("Data source")
    file = st.file_uploader("Upload CSV", type=["csv"])
    use_sample = st.checkbox("Use sample Iris", value=(file is None))

# Load
df = load_data(file, use_sample=use_sample)

if df.empty:
    st.info("No data yet. Upload a CSV or enable 'Use sample Iris' in the sidebar.")
    st.stop()

st.subheader("Preview")
st.dataframe(df.head())

# Filters
st.subheader("Filters")
cols = st.multiselect("Columns to keep", df.columns.tolist(), default=df.columns.tolist())
min_rows = st.slider("Minimum rows required (sanity check)", 0, len(df), 0)

df_f = apply_filters(df, columns=cols, min_rows=min_rows)
st.write(f"Rows after filters: {len(df_f)}")
st.dataframe(df_f.head())

# Plot
if len(df_f.columns) >= 2:
    st.subheader("Quick Plot")
    x = st.selectbox("X axis", df_f.columns, index=0)
    y = st.selectbox("Y axis", df_f.columns, index=min(1, len(df_f.columns)-1))
    fig = quick_plot(df_f, x, y)
    st.pyplot(fig)