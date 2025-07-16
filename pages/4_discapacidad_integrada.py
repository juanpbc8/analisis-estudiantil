import streamlit as st
from utils.carga_datos import cargar_datos
from utils.graficos import grafico_matriculas_discapacidad

# Título de la página
st.title("🧍‍♂️ Evolución por Tipo de Discapacidad Integrada")

# Cargar datos
df = cargar_datos()

# ====================== ESTADÍSTICAS ======================

df_discas = df[df['TipoDiscaIntegrada'].notna()]
conteo_discas = df_discas['TipoDiscaIntegrada'].value_counts()

tipo_mas_comun = conteo_discas.idxmax()
matriculas_mas_comun = conteo_discas.max()

tipo_menos_comun = conteo_discas.idxmin()
matriculas_menos_comun = conteo_discas.min()

col1, col2 = st.columns(2)
col1.metric("🔝 Discapacidad más reportada",
            f"{tipo_mas_comun} ({matriculas_mas_comun:,})")
col2.metric("🔻 Menos frecuente",
            f"{tipo_menos_comun} ({matriculas_menos_comun:,})")

# ====================== GRÁFICO ===========================

fig = grafico_matriculas_discapacidad(df)

col3, col4, col5 = st.columns([1, 2, 1])
with col4:
    st.pyplot(fig, use_container_width=False)

# ==================== DESCRIPCIÓN =========================

st.markdown("""
Este gráfico muestra cómo ha evolucionado la matrícula de estudiantes con algún tipo de **discapacidad integrada**  
en los servicios educativos entre 2021 y 2024. Se destacan las cinco discapacidades más reportadas en el sistema.
""")
