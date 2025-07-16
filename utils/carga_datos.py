import pandas as pd
import streamlit as st
from utils.limpieza import limpiar_dataframe


@st.cache_data
def cargar_datos():
    df = pd.read_csv("data/matricula_2021_2024_total.csv")
    df_limpio = limpiar_dataframe(df)
    return df_limpio
