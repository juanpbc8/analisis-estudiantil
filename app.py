import streamlit as st
from utils.carga_datos import cargar_datos

st.set_page_config(page_title="Análisis de Matrícula", layout="wide")

st.title("Análisis de Matrícula Escolar 2021 - 2024")
st.markdown("Selecciona una sección del menú lateral para comenzar.")

# Cargar una sola vez y se cachea
cargar_datos()
