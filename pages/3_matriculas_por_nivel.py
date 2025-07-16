import streamlit as st
from utils.carga_datos import cargar_datos
from utils.graficos import grafico_matriculas_por_nivel

# Título de la página
st.title("🎓 Evolución de Matrícula por Nivel Educativo")

# Cargar datos
df = cargar_datos()

# ====================== ESTADÍSTICAS ======================

# Calcular total por nivel
df_niveles = df['dsc_nivel'].value_counts().sort_values(ascending=False)

nivel_mas_alto = df_niveles.idxmax()
matriculas_mas_alto = df_niveles.max()

nivel_mas_bajo = df_niveles.idxmin()
matriculas_mas_bajo = df_niveles.min()

col1, col2 = st.columns(2)
col1.metric("🔝 Nivel más común", f"{nivel_mas_alto} ({matriculas_mas_alto:,})")
col2.metric("🔻 Nivel menos común",
            f"{nivel_mas_bajo} ({matriculas_mas_bajo:,})")

# ====================== GRÁFICO ===========================

fig = grafico_matriculas_por_nivel(df)

col3, col4, col5 = st.columns([1, 2, 1])
with col4:
    st.pyplot(fig, use_container_width=False)

# ==================== DESCRIPCIÓN =========================

st.markdown("""
Este gráfico representa la evolución de la matrícula escolar según el **nivel educativo**: Inicial, Primaria, Secundaria, etc.  
Permite detectar si hay una disminución en niveles superiores o cambios en la base escolar entre 2021 y 2024.
""")
