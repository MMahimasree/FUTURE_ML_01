import streamlit as st
import pandas as pd

df = pd.read_csv("Customer_Support.csv")
st.write(df)
