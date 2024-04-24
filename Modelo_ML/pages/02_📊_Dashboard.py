import streamlit as st
from IPython.display import IFrame

st.set_page_config(page_icon="📊", page_title="Dashboard McDonald's", layout="wide") # Pestaña navegador
st.image("https://i.imgur.com/cBlhTU9.png", width=200) # Logo
st.title("Dashboard") # titulo
st.markdown('***') # linea separadora

Dashboard = ('https://app.powerbi.com/view?r=eyJrIjoiZmYzMGI4NzctZDUzMS00NmJkLWJiMTMtY2I1MzhkMGIyZmY1IiwidCI6Ijk4YzUyOTJjLTZmODUtNDU2NS04YWNlLTk2OWRhZGE3ODgwOCIsImMiOjR9')
st.components.v1.iframe(Dashboard, width=1000, height=600)