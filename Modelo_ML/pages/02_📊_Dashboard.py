import streamlit as st
from IPython.display import IFrame

st.set_page_config(page_icon="📊", page_title="Dashboard McDonald's", layout="wide") # Pestaña navegador
st.image("https://i.imgur.com/cBlhTU9.png", width=200) # Logo
st.title("Dashboard") # titulo
st.markdown('***') # linea separadora



st.markdown('##### • Sedes: Visualiza métricas y análisis por sedes para comparar el rendimiento entre ubicaciones.')
st.markdown('##### • KPI: Destaca indicadores clave de rendimiento (KPI) con métricas anuales asociadas para evaluar el desempeño a lo largo del tiempo.')
st.markdown('##### • Rankings: Muestra varios "Top 3" identificando las mejores y peores sedes en cantidad de reseñas positivas y calificación promedio.')

st.markdown('***') # linea separadora

Dashboard = ('https://app.powerbi.com/view?r=eyJrIjoiZmYzMGI4NzctZDUzMS00NmJkLWJiMTMtY2I1MzhkMGIyZmY1IiwidCI6Ijk4YzUyOTJjLTZmODUtNDU2NS04YWNlLTk2OWRhZGE3ODgwOCIsImMiOjR9')
st.components.v1.iframe(Dashboard, width=1000, height=600)