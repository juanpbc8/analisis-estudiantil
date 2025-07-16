import streamlit as st
from utils.carga_datos import cargar_datos
from utils.graficos import grafico_total_matriculas

# Título de la página
st.title("📊 Total de Matrículas por Año")

# Cargar el DataFrame limpio desde caché
df = cargar_datos()

# ESTADÍSTICAS
conteo = df['año'].value_counts().sort_index()

total_matriculas = conteo.sum()
promedio_anual = int(conteo.mean())
anio_max = conteo.idxmax()
anio_min = conteo.idxmin()

col1, col2, col3, col4 = st.columns(4)
col1.metric("🔢 Total 2021–2024", f"{total_matriculas:,}")
col2.metric("📊 Promedio por Año", f"{promedio_anual:,}")
col3.metric("📈 Pico en", f"{anio_max} ({conteo[anio_max]:,})")
col4.metric("📉 Mínimo en", f"{anio_min} ({conteo[anio_min]:,})")

# GRÁFICO

fig = grafico_total_matriculas(df)

col5, col6, col7 = st.columns([1, 2, 1])
with col6:
    st.pyplot(fig, use_container_width=False)

# DESCRIPCION
st.markdown("""
Este gráfico muestra el **número total de matrículas escolares** registradas por año entre 2021 y 2024.  
Permite identificar variaciones generales en la participación del sistema educativo nacional a lo largo del tiempo.
""")
