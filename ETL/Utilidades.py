import pandas as pd

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