import pandas as pd
import os

# Ruta donde guardaste los archivos descargados
ruta_archivos = 'data/'

# Lista con nombres exactos de los archivos
archivos = [
    ('MatriculaAtraso_2021.csv', 2021),
    ('MatriculaAtraso_2022.csv', 2022),
    ('MatriculaAtraso_2023.csv', 2023),
    ('MatriculaAtraso_2024.csv', 2024)
]

# Lista para almacenar cada DataFrame
df_list = []

for archivo, anio in archivos:
    df = pd.read_csv(os.path.join(ruta_archivos, archivo))
    df['año'] = anio
    df_list.append(df)

# Unir todos los DataFrames
df_total = pd.concat(df_list, ignore_index=True)

# Guardar el conjunto completo para análisis
df_total.to_csv('matricula_2021_2024_total.csv', index=False)

print("Dataset combinado listo con", df_total.shape[0], "filas.")
