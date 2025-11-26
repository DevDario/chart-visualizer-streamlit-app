import streamlit as st
import pandas as pd

st.write("""
# Chart Visualizer App
""")

st.write("""
add your data file(CSV) to see
""")

df = pd.read_csv("my_data.csv")
df["data"] = pd.to_datetime(df["data"])
st.line_chart(df.set_index('data'))

