def normalizar_categorias(df):
    df['gestion'] = df['gestion'].str.strip().str.title()
    df['dsc_nivel'] = df['dsc_nivel'].str.strip().str.title()
    return df


def convertir_categorias(df):
    df['gestion'] = df['gestion'].astype('category')
    df['dsc_nivel'] = df['dsc_nivel'].astype('category')
    return df


def manejar_nulos(df):
    # Reemplazar NaN por 0 en columnas numéricas
    columnas_numericas = df.select_dtypes(include='number').columns
    df[columnas_numericas] = df[columnas_numericas].fillna(0)
    return df


def limpiar_dataframe(df):
    df = normalizar_categorias(df)
    df = convertir_categorias(df)
    df = manejar_nulos(df)
    return df
