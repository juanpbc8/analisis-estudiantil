import streamlit as st
from utils.carga_datos import cargar_datos
from utils.graficos import grafico_aprobados_desaprobados

# Título
st.title("📘 Evolución de Estudiantes Aprobados y Desaprobados")

# Cargar datos limpios
df = cargar_datos()

# =================== ESTADÍSTICAS ===================

df_suma = df.groupby('año')[['Aprobado', 'Desaprobado']].sum()

anio_max_apr = df_suma['Aprobado'].idxmax()
valor_max_apr = df_suma['Aprobado'].max()

anio_max_des = df_suma['Desaprobado'].idxmax()
valor_max_des = df_suma['Desaprobado'].max()

col1, col2 = st.columns(2)
col1.metric("✅ Año con más Aprobados", f"{anio_max_apr} ({valor_max_apr:,})")
col2.metric("❌ Año con más Desaprobados",
            f"{anio_max_des} ({valor_max_des:,})")

# ==================== GRÁFICO =====================

fig = grafico_aprobados_desaprobados(df)

col3, col4, col5 = st.columns([1, 2, 1])
with col4:
    st.pyplot(fig, use_container_width=False)

# ================== DESCRIPCIÓN ===================

st.markdown("""
Este gráfico muestra cómo ha evolucionado la cantidad de estudiantes **aprobados** y **desaprobados**  
entre los años 2021 y 2024.  
Permite analizar tendencias en el rendimiento académico a nivel nacional y detectar posibles impactos por región, pandemia u otros factores.
""")
