## Tecnologías utilizadas

- Python **3.10.11**
- [Streamlit](https://streamlit.io/) `1.46.1` – Web app interactiva
- [Pandas](https://pandas.pydata.org/) `2.3.1` – Manipulación de datos
- [Matplotlib](https://matplotlib.org/) `3.10.3` – Gráficos estáticos
- [Seaborn](https://seaborn.pydata.org/) `0.13.2` – Estadísticas visuales
- [Plotly](https://plotly.com/python/) `6.2.0` – Visualizaciones interactivas

## Datos

Este proyecto utiliza datos públicos del portal de datos abiertos del Perú:

🔗 Fuente: [Matrícula y Trayectoria Estudiantil 2021–2024](https://datosabiertos.gob.pe/dataset/matriculación-y-trayectoria-estudiantil-2021-2024)

### Pasos para preparar los datos:

1. Descarga los siguientes archivos CSV desde el enlace:
   - `MatriculaAtraso_2021.csv`
   - `MatriculaAtraso_2022.csv`
   - `MatriculaAtraso_2023.csv`
   - `MatriculaAtraso_2024.csv`

2. Colócalos dentro de la carpeta `/data`.

3. Ejecuta el script `combinar.py` para combinarlos en un único archivo llamado `matricula_2021_2024_total.csv`.

```bash
python combinar.py
