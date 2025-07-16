import matplotlib.pyplot as plt
import seaborn as sns


def grafico_total_matriculas(df):
    conteo = df['año'].value_counts().sort_index()

    fig, ax = plt.subplots(figsize=(6, 4))  # Tamaño más pequeño
    ax.bar(conteo.index.astype(str), conteo.values, color="#4C72B0")
    ax.set_title("Total de Matrículas por Año")
    ax.set_xlabel("Año")
    ax.set_ylabel("Cantidad de Matrículas")
    ax.tick_params(axis='x', labelrotation=0)
    fig.tight_layout()
    return fig


def grafico_matriculas_por_gestion(df):
    df_gestion = df.groupby(
        ['año', 'gestion']).size().reset_index(name='total')

    fig, ax = plt.subplots(figsize=(6, 4))  # Tamaño más pequeño
    sns.lineplot(data=df_gestion, x='año', y='total',
                 hue='gestion', marker='o', ax=ax)
    ax.set_title("Evolución de Matrícula por Gestión Educativa")
    ax.set_xlabel("Año")
    ax.set_ylabel("Cantidad de Matrículas")
    fig.tight_layout()
    return fig


def grafico_matriculas_por_nivel(df):
    # Agrupamos por año y nivel educativo
    df_nivel = df.groupby(['año', 'dsc_nivel']
                          ).size().reset_index(name='total')

    # Creamos el gráfico de líneas
    fig, ax = plt.subplots(figsize=(7, 4))
    sns.lineplot(data=df_nivel, x='año', y='total',
                 hue='dsc_nivel', marker='o', ax=ax)
    ax.set_title("Evolución de Matrícula por Nivel Educativo")
    ax.set_xlabel("Año")
    ax.set_ylabel("Cantidad de Matrículas")
    fig.tight_layout()
    return fig


def grafico_matriculas_discapacidad(df):
    # Filtramos solo registros con discapacidad no vacía
    df_filtrado = df[df['TipoDiscaIntegrada'].notna()]

    # Obtenemos los 5 tipos más frecuentes
    top5 = df_filtrado['TipoDiscaIntegrada'].value_counts().nlargest(
        5).index.tolist()

    # Filtramos el DataFrame solo con esos 5
    df_top = df_filtrado[df_filtrado['TipoDiscaIntegrada'].isin(top5)]

    # Agrupamos para graficar
    resumen = df_top.groupby(
        ['año', 'TipoDiscaIntegrada']).size().reset_index(name='total')

    # Creamos el gráfico
    fig, ax = plt.subplots(figsize=(7, 4))
    sns.lineplot(data=resumen, x='año', y='total',
                 hue='TipoDiscaIntegrada', marker='o', ax=ax)
    ax.set_title(
        "Evolución de Matrícula por Tipo de Discapacidad Integrada (Top 5)")
    ax.set_xlabel("Año")
    ax.set_ylabel("Cantidad de Matrículas")
    fig.tight_layout()
    return fig


def grafico_aprobados_desaprobados(df):
    # Agrupar por año y sumar ambos valores
    df_apr_des = df.groupby(
        'año')[['Aprobado', 'Desaprobado']].sum().reset_index()

    # Crear gráfico
    fig, ax = plt.subplots(figsize=(7, 4))
    sns.lineplot(data=df_apr_des, x='año', y='Aprobado',
                 marker='o', label='Aprobado', ax=ax)
    sns.lineplot(data=df_apr_des, x='año', y='Desaprobado',
                 marker='o', label='Desaprobado', ax=ax)

    ax.set_title("Evolución de Estudiantes Aprobados y Desaprobados")
    ax.set_xlabel("Año")
    ax.set_ylabel("Cantidad de Estudiantes")
    ax.legend(title="Situación Final")
    fig.tight_layout()
    return fig
