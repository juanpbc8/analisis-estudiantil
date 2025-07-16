import streamlit as st
from utils.carga_datos import cargar_datos
from utils.graficos import grafico_total_matriculas, grafico_matriculas_por_gestion

st.title("Evolución de la Matrícula Escolar 2021 - 2024")

df = cargar_datos()

st.subheader("1. Total de Matrículas por Año")
fig1 = grafico_total_matriculas(df)
st.pyplot(fig1, use_container_width=False)
st.markdown("Este gráfico muestra el volumen total de estudiantes matriculados por año, lo cual permite observar tendencias generales del sistema educativo.")

st.subheader("2. Evolución de Matrículas por Tipo de Gestión")
fig2 = grafico_matriculas_por_gestion(df)
st.pyplot(fig2, use_container_width=False)
st.markdown("Aquí se observa cómo han evolucionado las matrículas en instituciones educativas públicas y privadas entre 2021 y 2024.")
