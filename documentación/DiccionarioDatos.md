# Diccionario de datos:

## Google Maps:

### metadatos-sitios.csv:

Archivo formato .csv que contiene la metadata. Contiene la información del comercio incluyendo nombre, descripción, localización, atributos, categorias y estado del negocio.

* 'name': string, nombre del comercio.

```python
        'name': 'Walgreens Pharmacy'
```

* 'address': string, dirección del comercio.

```python
        'address': 'Walgreens Pharmacy, 124 E North St, Kendallville, IN 46755'
```

* 'gmap_id': string, identificador unico del comercio en Google Maps.

```python
        'gmap_id': '0x881614ce7c13acbb:0x5c7b18bbf6ec4f7e'
```

* 'description': string, breve descripción del comercio.

```python
        'description': 'Department of the Walgreens chain providing prescription medications & other health-related items.'
```

* 'latitude': float, coordenada de latitud del comercio en Google Maps.

```python
        'latitude': 41.451859999999996
```

* 'longitude': float, coordenada de longitud del comercio en Google Maps.

```python
        'latitude': -85.2666757
```

* 'category': list, lista con las categorias a las que pertenece el comercio.

```python
        'category': ['Pharmacy']
```
* 'avg_rating': float, puntuación promedio del comercio.

```python
        'avg_rating': 4.2
```

* 'num_of_reviews': integer, cantidad de reseñas del comercio.

```python
        'num_of_reviews': 5
```

* 'price': string, rango del costo del comercio.

```python
        'price': '$$'
```

* 'hours': list, horario de apertura y cierre del comercio.

```python
        'hours': [['Thursday', '8AM–1:30PM'], ['Friday', '8AM–1:30PM'], ['Saturday', '9AM–1:30PM'], ['Sunday', '10AM–1:30PM'], ['Monday', '8AM–1:30PM'], ['Tuesday', '8AM–1:30PM'], ['Wednesday', '8AM–1:30PM']]
```

* 'MISC': object, diccionario con caracteristicas o servicios adicionales del comercio.

```python
    'MISC': {'Service options': ['Curbside pickup', 'Drive-through', 'In-store pickup', 'In-store shopping'], 
    'Health & safety': ['Mask required', 'Staff wear masks', 'Staff get temperature checks'], 
    'Accessibility': ['Wheelchair accessible entrance', 'Wheelchair accessible parking lot'], 
    'Planning': ['Quick visit'], 
    'Payments': ['Checks', 'Debit cards']}
```

* 'state': string, estado del comercio.

```python
        'state': 'Closes soon ⋅ 1:30PM ⋅ Reopens 2PM'
```

* 'relative_results': list, lista con resultados de busqueda relacionados al comercio.

```python
        'relative_results': ['0x881614cd49e4fa33:0x2d507c24ff4f1c74', '0x8816145bf5141c89:0x535c1d605109f94b', '0x881614cda24cc591:0xca426e3a9b826432', '0x88162894d98b91ef:0xd139b34de70d3e03', '0x881615400b5e57f9:0xc56d17dbe420a67f']
```

* 'url': string, link a la ubicación del comercio en Google Maps.

```python
        'url': 'https://www.google.com/maps/place//data=!4m2!3m1!1s0x881614ce7c13acbb:0x5c7b18bbf6ec4f7e?authuser=-1&hl=en&gl=us'
```


### review-Florida.csv:

Archivo en formato .csv donde se disponibilizan las reviews de los usuarios en el estado de Florida, incluyendo información del usuarios como nombre, identificador unico del usuario, reseña, puntuación y identificador unico del comercio en Google Maps.

* 'user_id': string, identificador unico del usuario.

```python
        'user_id': '101463350189962023774'
```

* 'name': string, nombre del usuario.

```python
        'name': 'Jordan Adams'
```

* 'time': integer, horario en el que se realizo la reseña.

```python
        'time': 1627750414677
```

* 'rating': integer, puntaje en estrellas del 1 al 5, dado por el usuario al comercio.

```python
        'rating': 5
```

* 'text': string, reseña del usuario al comercio.

```python
        'text': 'Cool place, great people, awesome dentist!'
```

* 'pics': object, link a la foto subida por el usuario.

```python
        'pics': [
        {
        'url': ['https://lh5.googleusercontent.com/p/AF1QipNq2nZC5TH4_M7h5xRAd61hoTgvY1o9lozABguI=w150-h150-k-no-p']
        }
                ]
```

* 'resp': object, respuesta del comercio al usuario, con el horario en el que fue posteada y el texto.

```python
        'resp': {
                'time': 1628455067818, 
                'text': 'Thank you for your five-star review! -Dr. Blake'
                }
```

* 'gmap_id': string, identificador unico del comercio en Google Maps.

```python
        'gmap_id': '0x87ec2394c2cd9d2d:0xd1119cfbee0da6f3'
```


## Yelp!

### business.csv:

Archivo formato .csv que contiene la información del comercio incluyendo nombre, descripción, localización, atributos, categorias y estado del negocio.

* 'business_id': string, identificador unico del comercio en Yelp.

```python
        'business_id': 'tnhfDv5Il8EaGSXZGiuQGg'
```

* 'name': string, nombre del comercio.

```python
        'name': 'Garaje'
```

* 'address': string, dirección completa del comercio.

```python
        'address': '475 3rd St'
```

* 'city': string, ciudad donde se ubica el comercio.

```python
        'city': 'San Francisco'
```

* 'state': string, codigo de dos letras del Estado donde se ubica el comercio.

```python
        'state': 'CA'
```

* 'postal code': string, codigo postal correspondiente a la ubicación del comercio.

```python
        'postal code': '94107'
```

* 'latitude': float, coordenada de latitud del comercio.

```python
        'latitude': 37.7817529521
```

* 'longitude': float, coordenada de longitud del comercio.

```python
        'longitude': -122.39612197
```

* 'stars': float, puntaje en estrellas del 1 al 5, dado por el usuario al comercio, redondeado a 0 o 0.5.

```python
        'stars': 4.5
```

* 'review_count': integer, cantidad de reseñas.

```python
        'review_count': 1198
```

* 'is_open': integer, hace referencia a si el comercio se encuentra en funcionamiento o no. 0 si esta cerrado, 1 si esta abierto.

```python
        'is_open': 1
```

* 'attributes': object, atributos del negocio.

```python
        'attributes': {
    "RestaurantsTakeOut": true,
    "BusinessParking": {
        "garage": false,
        "street": true,
        "validated": false,
        "lot": false,
        "valet": false
    },
}
```

* 'categories': list, lista de las categorias a las que pertenece el comercio.

```python
        'categories': [
    "Mexican",
    "Burgers",
    "Gastropubs"
]
```

* 'hours': object, horario de apertura y cierre del comercio.

```python
        'hours': {
    "Monday": "10:00-21:00",
    "Tuesday": "10:00-21:00",
    "Friday": "10:00-21:00",
    "Wednesday": "10:00-21:00",
    "Thursday": "10:00-21:00",
    "Sunday": "11:00-18:00",
    "Saturday": "10:00-21:00"
    }
```

### review.csv:

Archivo formato .csv que contiene las reseñas completas, incluyendo el user_id que escribió el review y el business_id por el cual se escribe la reseña.

* 'review_id': string, 22 caracteres, identificador unico de la reseña.

```python
        'review_id': 'zdSx_SD6obEhz9VrW9uAWA'
```

* 'user_id': string, 22 caracteres, identificador unico del usuario.

```python
        'user_id': 'Ha3iJu77CxlrFm-vQRs_8g'
```

* 'business_id': string, 22 caracteres, identificador unico del comercio.

```python
        'business_id': 'tnhfDv5Il8EaGSXZGiuQGg'
```

* 'stars': integer, puntaje en estrellas del 1 al 5, dado por el usuario al comercio.

```python
        'stars': 4
```

* 'date': string, fecha en la que se realizo la reseña, en formato YYYY-MM-DD.

```python
        'date': '2016-03-09'
```

* 'text': string, reseña del usuario al comercio.

```python
        'text': "Great place to hang out after work: the prices are decent, and the ambience is fun. It's a bit loud, but very lively. The staff is friendly, and the food is good. They have a good selection of drinks."
```

* 'useful': integer, número de votos como reseña util.

```python
        'useful': 0
```

### tip.csv:

Archivo formato .csv que contiene tips (consejos), escritos por los usuarios incluyendo información del usuario y del comercio. Las tips son más cortas que las reseñas y tienden a dar sugerencias rapidas.

* 'text': string, texto del tip. 

```python
        'text': "Secret menu - fried chicken sando is da bombbbbbb Their zapatos are good too."
```

* 'date': string, fecha en la que se escribio el tip, en formato YYYY-MM-DD. 

```python
        'date': 'YYYY-MM-DD'
```

* 'compliment_count': integer, cantidad de cumplidos que tiene el tip. 

```python
        'compliment_count': 172
```

* 'business_id': string, f22 caracteres, identificador unico del comercio. 

```python
        'business_id': 'tnhfDv5Il8EaGSXZGiuQGg'
```

* 'user_id': string, 22 caracteres, identificador unico del usuario. 

```python
        'user_id': '49JhAJh8vSQ-vM4Aourl0g'
```

