def normalizacion_columnas(df):
    '''
    Función que recibe como parametro un DataFrame 
    y retorna las columnas normalizadas, con el formato de titulo.
    
    '''
    df.columns = df.columns.str.title()
    return df