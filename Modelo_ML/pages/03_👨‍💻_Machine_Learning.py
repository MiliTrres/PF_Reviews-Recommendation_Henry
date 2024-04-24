from fastapi import HTTPException
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from scipy.sparse import vstack
import numpy as np
import pandas as pd
from wordcloud import WordCloud
import re
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from collections import Counter
import streamlit as st
import tempfile

st.set_page_config(page_icon="👨‍💻", page_title="Machine Learning", layout="wide") # Pestaña navegador
st.image("https://i.imgur.com/cBlhTU9.png", width=200) # Logo
st.title("Machine Learning McDonald's") # titulo
st.markdown('***') # linea separadora

# Logo en la barra lateral  
#st.sidebar.image("https://i.imgur.com/cBlhTU9.png")
st.sidebar.markdown('Panel al lado izquierdo')

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('stopwords')

reviews = pd.read_csv('reviews.csv')
models_by_branch = joblib.load('all_models.joblib')
stopwords = set(stopwords.words('english'))

#///////////// SENTIMENT ANALYSIS /////////////
if st.checkbox('Sentiment analysis'):
    # Informacion de funcion
    st.markdown('''
            Función que recibe como parametro la dirección exacta de una sucursal y retorna la cantidad de reseñas positivas, neutras y negativas para esa sucursal.  
            Args:  
                location (str): Dirección exacta de la sucursal.  
            Returns:  
                dict: Diccionario con la cantidad de reseñas positivas, neutras y negativas.  
            Ejemplo:  
                1590 Missouri Ave
            ''')
    # Input de sucursal a buscar
    title = st.text_input('sentiment',value='',placeholder='sentiment_analysis',key='text_input')
    
    
    def sentiment_analysis(location: str):
            '''
            Función que recibe como parametro la dirección exacta de una sucursal y retorna la cantidad de reseñas positivas, neutras y negativas para esa sucursal.
            Args:
                location (str): Dirección exacta de la sucursal.
            Returns:
                dict: Diccionario con la cantidad de reseñas positivas, neutras y negativas.
            Ejemplo:
                1590 Missouri Ave
            '''
            try:
                # Normalizamos la dirección ingresada para que se puedan comparar con las direcciones en el archivo correctamente.
                location = title

                # Verificamos si la sucursal está en el archivo de reseñas.
                if location not in reviews['address'].values:
                    raise HTTPException(status_code=404, detail=f"Sucursal '{location}' no encontrada")
                
                # Filtramos las reseñas de la sucursal especificada
                reviews_by_branch = reviews[reviews['address'] == location]

                # Contamos la cantidad de reseñas positivas, neutras y negativas
                positive_reviews = reviews_by_branch[reviews_by_branch['rating'] >= 3.0].shape[0]
                neutral_reviews = reviews_by_branch[reviews_by_branch['rating'] == 3.0].shape[0]
                negative_reviews = reviews_by_branch[reviews_by_branch['rating'] < 3.0].shape[0]

                result = f"Total de reseñas: {reviews_by_branch.shape[0]}\n\n" \
                 f"Reseñas positivas: {positive_reviews}\n\n" \
                 f"Reseñas neutras: {neutral_reviews}\n\n" \
                 f"Reseñas negativas: {negative_reviews}"

                # Mostramos el resultado con formato Markdown
                st.markdown(result)

            except Exception as e:
                    raise HTTPException(status_code=500, detail=str(e))

    # Botones de Reset y Mostrar Resultado
    if st.button("Reset", type="primary", key='reset_button'):
        title = ''  # Vaciar el campo de entrada de texto
    if st.button('Mostrar resultado', key='show_result_button'):
        if title:
            st.write(sentiment_analysis(title))
        else:
            st.warning("Por favor, ingresa una dirección correcta.")

#///////////// GET TOP WORDS /////////////
if st.checkbox('Get top words'):

    # Informacion de funcion
    '''
        Función que recibe como parametro la dirección exacta de una sucursal y retorna las palabras más frecuentes en las reseñas bajas de esa sucursal, en una nube de palabras.  
        Args:  
            location (str): Dirección exacta de la sucursal.  
        Returns:  
            StreamingResponse: Imagen en formato PNG con la nube de palabras.  
        Ejemplo:  
            1485 Commercial Way 
        '''
    
    # Input de sucursal a buscar
    title = st.text_input('get top words', placeholder='get top words')
    def get_top_words(location: str):
        '''
        Función que recibe como parametro la dirección exacta de una sucursal y retorna las palabras más frecuentes en las reseñas bajas de esa sucursal, en una nube de palabras.
        Args:
            location (str): Dirección exacta de la sucursal.
        Returns:
            StreamingResponse: Imagen en formato PNG con la nube de palabras.
        Ejemplo:
            1485 Commercial Way
        '''
        try:
            # Normalizamos la dirección ingresada para que se puedan comparar con las direcciones en el archivo correctamente.
            location = title
            reviews = pd.read_csv('reviews.csv')

            # Filtramos las reseñas por la sucursal especificada y con rating menor a 3.0.
            reviews = reviews[(reviews['address'] == location) & (reviews['rating'] < 3.0)]['text']

            # Preprocesamos de las reseñas.
            processed_reviews = [' '.join([token for token in word_tokenize(re.sub(r'[^a-zA-Z0-9\s]', '', str(review))) if token.lower() not in stopwords]) for review in reviews]

            # Unimos todas las reseñas en un solo texto
            full_text = ' '.join(processed_reviews)

            # Contamos la frecuencia de las palabras
            word_freq = Counter(full_text.split())

            # Creamos la nube de palabras
            wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(word_freq)

            # Guardar la imagen en un archivo temporal
            with tempfile.NamedTemporaryFile(suffix='.png', delete=False) as temp_file:
                image_path = temp_file.name
                wordcloud.to_file(temp_file.name)

            # Retornamos la ruta del archivo temporal
            return image_path

        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    # Botones de Reset y Mostrar Resultado
    if st.button("Reset", key='reset_button'):
        title = ''  # Vaciar el campo de entrada de texto
    if st.button('Mostrar resultado', key='show_result_button'):
        if title:
            image_path = get_top_words(title)
            st.image(image_path)
        else:
            st.warning("Por favor, ingresa una dirección correcta.")

#///////////// FUNCION AUXILIAR PARA ML /////////////
def get_reviews_by_local(local_name):
    '''
    Función que recibe como parametro la dirección exacta de una sucursal y retorna las reseñas con rating menor a 3.0 y las reseñas con rating mayor o igual a 3.0.

    '''
    reviews_low = []
    reviews_high = []

    archivo = reviews

    for index, row in archivo.iterrows():
        if row['address'] == local_name:
            rating = row['rating']
            text = row['text']

            if pd.isnull(text):
                continue

            reviews_data = {'text': row['text'], 'rating': row['rating']}  
            if rating < 3.0:
                reviews_data['rating_category'] = 0

                if reviews_data['text'] != '':
                    reviews_low.append(reviews_data)

            elif rating >= 3.0:
                reviews_data['rating_category'] = 1

                if reviews_data['text'] != '':
                    reviews_high.append(reviews_data)
            
    return reviews_low, reviews_high

#///////////// FUNCION AUXILIAR PARA ML /////////////
def create_tfidf_matrix(reviews_low, reviews_high):
    '''
    Función que recibe como parametro las reseñas con rating menor a 3.0 y las reseñas con rating mayor o igual a 3.0 y retorna la matriz tfidf de las reseñas.
    
    '''

    all_reviews_text = [review['text'] for review in reviews_low] + [review['text'] for review in reviews_high]

    vectorizer = TfidfVectorizer()

    vectorizer.fit(all_reviews_text)

    tfidf_matrix_low = vectorizer.transform([review['text'] for review in reviews_low])

    tfidf_matrix_high = vectorizer.transform([review['text'] for review in reviews_high])

    return tfidf_matrix_low, tfidf_matrix_high

#///////////// PREDICT SCORE INCREMENT /////////////
if st.checkbox('Predict score increment'):
    # Informacion de funcion
    '''
        Función que recibe como parametro la dirección exacta de una sucursal y retorna el puntaje promedio actual, el incremento del puntaje y el puntaje promedio con incremento.  
        Args:  
            location (str): Dirección exacta de la sucursal.  
        Returns:  
            dict: Diccionario con el puntaje promedio actual, el incremento del puntaje, el porcentaje de incremento y el puntaje promedio con incremento.  
        Ejemplo:  
            9814 International Dr 
        '''
    # Input de sucursal a buscar
    title = st.text_input('Predict score increment',key='text_input', placeholder='Predict',)
    def predict_score_increment(location: str):
        '''
        Función que recibe como parametro la dirección exacta de una sucursal y retorna el puntaje promedio actual, el incremento del puntaje y el puntaje promedio con incremento.
        Args:
            location (str): Dirección exacta de la sucursal.
        Returns:
            dict: Diccionario con el puntaje promedio actual, el incremento del puntaje, el porcentaje de incremento y el puntaje promedio con incremento.
        Ejemplo:
            9814 International Dr 
        '''
        try:
            # Normalizamos la dirección ingresada para que se puedan comparar con las direcciones en el archivo correctamente.
            location = title

            # Verificamos si la sucursal está en el diccionario de modelos
            if location not in models_by_branch:
                raise HTTPException(status_code=404, detail=f"Modelo para la sucursal '{location}' no encontrado")

            # Obtenemos el modelo correspondiente a la sucursal
            model = models_by_branch[location]

            # Obtenemos las reseñas de la sucursal
            reviews_low, reviews_high = get_reviews_by_local(location)

            # Creamos la matriz tfidf
            tfidf_matrix_low, tfidf_matrix_high = create_tfidf_matrix(reviews_low, reviews_high)
            tfidf_matrix = vstack((tfidf_matrix_low, tfidf_matrix_high))

            # Creamos el vector de variables objetivo
            target_variable_low = np.zeros(tfidf_matrix_low.shape[0])
            target_variable_high = np.ones(tfidf_matrix_high.shape[0])

            # Unimos los vectores de variables objetivo
            target_variable = np.concatenate((target_variable_low, target_variable_high))

            # Obtenemos las predicciones del modelo
            original_ratings = [review['rating'] for review in reviews_low] + [review['rating'] for review in reviews_high]
            predicted_increases = model.predict(tfidf_matrix)
            updated_ratings = [original + increase for original, increase in zip(original_ratings, predicted_increases)]
            score_increment_percentage = (np.mean(predicted_increases) / np.mean(original_ratings)) * 100
            

            resultado = f"Puntaje actual: {round(np.mean(original_ratings), 2)}\n\n" \
                    f"Incremento del puntaje predicho: {round(np.mean(predicted_increases), 2)}\n\n" \
                    f"Porcentaje de incremento predicho: {round(score_increment_percentage, 2)}%\n\n" \
                    f"Puntaje promedio con incremento: {round(np.mean(updated_ratings), 2)}"
            st.markdown(resultado)
        
        except FileNotFoundError:
            raise HTTPException(status_code=404, detail=f"Modelo para la sucursal '{location}' no encontrado")
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
        
    # Botones de Reset y Mostrar Resultado
    if st.button("Reset", key='reset_button'):
        title = ''  # Vaciar el campo de entrada de texto
    if st.button('Mostrar resultado', key='show_result_button'):
        if title:
            st.write(predict_score_increment(title))
        else:
            st.warning("Por favor, ingresa una dirección correcta.")

# Genera linea separadora
st.markdown('***')
st.write('prueba....')