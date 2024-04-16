import pandas as pd
import ast
import numpy as np

def tipo_dato(df):
    
    """
    Función para obtener el tipo de dato de cada columna y el porcentaje de datos nulos.
    El argumento 'df' es el dataframe que se va a examinar.
    Recibe como parametro un DataFrame y retorna un DataFrame con los datos anteriormente mencionados.
    """
    # Se crea un diccionario para almacenar la información sobre las columnas
    diccionario_columnas = {"columna": [], "tipo_dato": [], "porcentaje_nulos": []}
    
    # Se itera a través de las columnas del dataframe
    for columna in df.columns:
        # Se calcula el porcentaje de valores no nulos en la columna actual
        porcentaje_no_nulos = (df[columna].count() / len(df) * 100)

        ### Se agrega la información al diccionario
        
        # Se añade el nombre de la columna al diccionario 'diccionario_columnas'
        diccionario_columnas["columna"].append(columna)  
        # Se obtiene el tipo de dato y se agrega al diccionario en la columna 'tipo_dato'
        diccionario_columnas["tipo_dato"].append(df[columna].apply(type).unique())  
        # Se calcula el porcentaje de nulos y se agrega al diccionario en la columna 'porcentaje_nulos'
        diccionario_columnas["porcentaje_nulos"].append(round(100 - porcentaje_no_nulos, 2))  

    # Se crea un dataframe con la información recopilada
    df_info = pd.DataFrame(diccionario_columnas)

    # Se devuelve el dataframe con la información sobre las columnas
    return df_info

def registros_duplicados(df):
    '''
    Función que recibe como parametro un DataFrame
    y retorna un DataFrame con los registros duplicados.
    
    '''
    df = df[df.duplicated(keep=False)]
    return df


def horas_business(df):
    '''
    '''
    if isinstance(df, str):
        try:
            return eval(df)
        except ValueError:
            return {}
    else:
        return {}
    
def horas_metada(df):
    """
    Extrae columnas de la columna 'hours' en el DataFrame.
    Devuelve un nuevo DataFrame con las columnas extraídas.
    Los valores nulos se rellenan con 'Sin datos'.
    """

    # Convertir diccionarios en formato de cadena a diccionarios reales
    df['hours'] = df['hours'].apply(lambda x: ast.literal_eval(x) if isinstance(x, str) else None)

    # Convertir listas a diccionarios
    df['hours'] = df['hours'].apply(lambda x: dict(x) if isinstance(x, list) else None)

    # Extraer columnas de la columna 'hours'
    hours_df = df['hours'].apply(pd.Series)

    # Rellenar valores nulos con 'Sin datos'
    hours_df = hours_df.fillna('Sin datos')

    # Concatenar las columnas al DataFrame original
    df = pd.concat([df, hours_df], axis=1)

    # Eliminar la columna original 'hours'
    df = df.drop(columns=['hours'])

    return df

def categoria_metadatos(df):
    """
    Formatea la columna 'category' en el DataFrame.
    Convierte las cadenas de lista en listas reales y las une en una sola cadena separada por comas.
    Los valores no válidos se reemplazan por NaN.
    """

    # Convierte las cadenas de lista en listas reales
    df['category'] = df['category'].apply(lambda x: ast.literal_eval(x) if isinstance(x, str) else np.nan)

    # Formatea las listas en una sola cadena separada por comas
    df['category'] = df['category'].apply(lambda x: ', '.join(x) if isinstance(x, list) else x)

    return df

def extract_address(address):
    '''
    Función que recibe como parametro una cadena de texto y retorna la dirección.
    '''
    
    parts = address.split(',')
    if len(parts) >= 2:
        return parts[1].strip()
    else:
        return None
    

