import streamlit as st
import pandas as pd
from google.cloud import storage
import gcsfs

st.set_page_config(page_icon="📊", page_title="Mejorando McDonald's", layout="wide")
st.image("https://i.imgur.com/cBlhTU9.png", width=200)
st.title("Proyecto de Análisis de Datos y Machine Learning McDonald's")


# Crea una instancia del cliente de almacenamiento
storage_client = storage.Client()

# Especifica el nombre de tu bucket
bucket_name = 'prueba-data-streamlit'

# Especifica el nombre del archivo en el bucket
file_name = 'modelo_recomendacion.parquet'

# Obtiene una referencia al bucket
bucket = storage_client.get_bucket(bucket_name)

# Construye la URL del archivo en el bucket
file_url = f"gs://{bucket_name}/{file_name}"

# Crea un objeto gcsfs para leer el archivo directamente desde el bucket
fs = gcsfs.GCSFileSystem(project='regal-stone-421121')

# Lee el archivo utilizando pandas
with fs.open(file_url) as f:
    df_modelo = pd.read_parquet(f)


# # # # # # # # # funcion 6: recomendacion_juego # # # # # # # # #

def recomendacion_juego(item_id):
    ''' 
    Esta función se encarga de obtener una lista de juegos recomendados para un usuario a partir del ID de un juego que le gusta.
    La función utiliza un modelo de recomendación pre-entrenado basado en la similitud entre juegos.

    Parámetros:
        item_id (int): El ID del juego que el usuario ha indicado que le gusta.
    Retorna:
        Una lista con 5 juegos recomendados similares al ingresado.
    '''
    # Filtrar el DataFrame por el año especificado
    df_filtro = df_modelo[df_modelo['item_id'] == item_id]
    
    resultado = df_filtro['Recomendaciones']
 
    return resultado



# Genera titulo
st.title('Introduccion a Streamlit')

# Genera linea separadora
st.markdown('***')
st.markdown('## Para que sirve streamlit?')
# Genera texto
st.write('texto de ejemplo')

st.sidebar.markdown('Panel al lado izquierdo')