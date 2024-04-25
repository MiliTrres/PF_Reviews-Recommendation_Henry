import streamlit as st
import pandas as pd

st.set_page_config(page_icon="🏠", page_title="Proyecto final soyHenry", layout="wide") # Pestaña navegador
st.image("https://i.imgur.com/cBlhTU9.png", width=400) # Logo
st.title("Proyecto de Análisis de Datos y Machine Learning para McDonald's") # titulo
st.markdown('***') # linea separadora

# Area texto de informacion
st.text_area(
    'Proyecto final del Bootcamp soyHenry, Abril 2024.',
    'En este documento vas a encontrar un registro sobre el proceso del proyecto final realizado por nuestro grupo.\n'  
    'Para ver la documentación del proyecto pueden acceder a nuestro repositorio de github: https://github.com/DJChincuini/PF_Reviews-Recommendation_Henry.'
    )

# Crea dos columnas
col1, col2 = st.columns(2)

with col1:
    st.write('''McDonald 's, una de las principales cadenas de comida rápida a nivel mundial, nos ha contactado ya que se encuentra desarrollando un nuevo sistema de incentivos para sus 
         empleados en el estado de Florida como parte de su programa para la constante mejora del servicio al cliente. ''')
    st.write('''Nuestra labor será evaluar los resultados del programa generando KPI’s y modelos predictivos acordes para dar el feedback correspondiente a nuestro cliente. ''') 
   

with col2:
   st.image('../Img/lovin.png', width = 200)
st.markdown('***') # linea separadora 	

st.title("¿Quiénes somos?") # titulo
st.write('Somos **Data Feedback Solutions**, un equipo especializado en transformar la voz de tus clientes en insights que ayudarán a llevar a tu empresa al siguiente nivel. Data Feedback Solutions se conforma por los siguientes profesionales:')

data = {
    'Nombre': ['Milagros Torres', 'Alejandra Monroy', 'Dante Chincuini', 'Rafael Oropeza', 'Jonathan Zegarra'],
    'Rol': ['Data Scientist', 'Data Scientist', 'Data Scientist', 'Data Scientist', 'Data Scientist']
}
df = pd.DataFrame(data)
st.table(df)