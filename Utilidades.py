import pandas as pd

def porcentaje_valores_nulos(dataframe):
    '''
    Función que recibe como parametro un DataFrame
    y retorna el porcentaje de valores nulos por columna.

    '''
    total_filas = dataframe.shape[0]
    porcentaje_nulos = (dataframe.isnull().sum() / total_filas) * 100
    
    for columna, porcentaje in porcentaje_nulos.items():
        print(f'La columna {columna} tiene un {porcentaje: .2f} % de valores nulos')
        

def registros_duplicados(df):
    '''
    Función que recibe como parametro un DataFrame
    y retorna un DataFrame con los registros duplicados.
    
    '''
    df = df[df.duplicated(keep=False)]
    return df

def agrupar_categorias(row):
    if pd.isnull(row):
        return 'Otros'  
    if 'restaurant' in row.lower():
        return 'Restaurantes'
    if 'coffee' in row.lower():
        return 'Cafeterías'
    elif 'nail' in row.lower() or 'spa' in row.lower() or 'beauty' in row.lower():
        return 'Belleza'
    else:
        return 'Otros'