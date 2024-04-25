from fastapi import FastAPI, HTTPException
from google.cloud import storage
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from scipy.sparse import vstack
import numpy as np
import pandas as pd
import os
from wordcloud import WordCloud
import io
import re
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from collections import Counter
from fastapi.responses import StreamingResponse

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('stopwords')


app = FastAPI()

reviews = pd.read_csv('reviews.csv')

models_by_branch = joblib.load('all_models.joblib')

stopwords = set(stopwords.words('english'))



@app.get("/sentiment_analysis/{location}")
async def sentiment_analysis(location: str):
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
        location = location.title()

        # Verificamos si la sucursal está en el archivo de reseñas.
        if location not in reviews['address'].values:
            raise HTTPException(status_code=404, detail=f"Sucursal '{location}' no encontrada")
        

        # Filtramos las reseñas de la sucursal especificada
        reviews_by_branch = reviews[reviews['address'] == location]

        # Contamos la cantidad de reseñas positivas, neutras y negativas
        positive_reviews = reviews_by_branch[reviews_by_branch['rating'] >= 3.0].shape[0]
        neutral_reviews = reviews_by_branch[reviews_by_branch['rating'] == 3.0].shape[0]
        negative_reviews = reviews_by_branch[reviews_by_branch['rating'] < 3.0].shape[0]

        return {"Total de reseñas": reviews_by_branch.shape[0],
                "Reseñas positivas": positive_reviews,
                "Reseñas neutras": neutral_reviews,
                "Reseñas negativas": negative_reviews}

    except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))


@app.get("/get_top_words")
async def get_top_words(location: str):
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
        location = location.title()

        # Leemos el archivo de reseñas
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

        # Guardar la imagen en un buffer
        img_buffer = io.BytesIO()
        wordcloud.to_image().save(img_buffer, format="PNG")
        img_buffer.seek(0)

        # Retornamos la imagen en formato PNG como un StreamingResponse
        return StreamingResponse(img_buffer, media_type="image/png")

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))



@app.get("/predict_score_increment/{location}")
async def predict_score_increment(location: str):
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
        location = location.title()

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
        

        return {"Puntaje actual": round(np.mean(original_ratings), 2),
                "Incremento del puntaje predicho": round(np.mean(predicted_increases), 2),
                "Porcentaje de incremento predicho": f"{round(score_increment_percentage, 2)}%",
                "Puntaje promedio con incremento": round(np.mean(updated_ratings), 2)}

    except FileNotFoundError:
        raise HTTPException(status_code=404, detail=f"Modelo para la sucursal '{location}' no encontrado")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
# Funciones auxiliares

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