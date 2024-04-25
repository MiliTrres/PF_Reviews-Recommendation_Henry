![Portada](https://i.imgur.com/hFWnAnb.jpeg)

<h1 align="center"><b>Proyecto de Análisis de Datos y Machine Learning McDonald's</b></h1>

## Contexto

McDonald's, una de las principales empresas de comida rápida a nivel global, está implementando un sistema de incentivos para sus empleados en el estado Florida como parte de su compromiso continuo con la mejora del servicio al cliente. Este piloto no solo reconoce el desempeño excepcional del equipo, sino que también busca evaluar la efectividad del sistema en un entorno operativo real. McDonald's espera que estos incentivos fortalezcan su posición como líder en la industria y mejoren la experiencia del cliente en sus locales del estado Florida y más allá.

<p align='center'> <img src="Img\Img-Mc.jpg" width="1000" height="300" ><p>

## Estructura

El presente proyecto cuuenta con las siguientes carpetas y archivos:

- [Datos](https://github.com/DJChincuini/PF_Reviews-Recommendation_Henry/tree/main/Datos): Contiene archivos en formato .parquet filtrados por los datos de interes utilizados para la realización del EDA.
- [ETL](https://github.com/DJChincuini/PF_Reviews-Recommendation_Henry/tree/main/ETL): Contiene los archivos utilizados para la realización del ETL de manera local.
- [Img](https://github.com/DJChincuini/PF_Reviews-Recommendation_Henry/tree/main/Img): Contiene imagenes utilizadas durante el desarrollo del proyecto.
- [Documentación](https://github.com/DJChincuini/PF_Reviews-Recommendation_Henry/tree/main/documentaci%C3%B3n): Contiene la documentación generada durante la realización del proyecto, como el diccionario de datos, el stack tecnológico, ciclo de vida del dato, entre otros.
- [_pycache_](https://github.com/DJChincuini/PF_Reviews-Recommendation_Henry/tree/main/__pycache__): Contiene archivos de caché que contienen código compilado en formato bytecode. Estos archivos se generan automáticamente por el intérprete de Python.

## ¿Quienes somos?

En Data Feedback Solutions somos tu aliado estratégico, dedicados a convertir la opinión de tus clientes en datos valiosos. Nuestro objetivo es llevar tu negocio al siguiente nivel, proporcionándote insights precisos y relevantes para impulsar tu éxito.

<p align='center'> <img src="Img\logo.jpg" alt="Accidente vial" width="300" height="300" ><p>

## Objetivo general y alcance

Data Feedback Solutions ha sido contratada por McDonald's con el objetivo de mejorar el rendimiento de sus locales en el estado de Florida y asegurar que cada visita sea una experiencia que haga decir 'Me encanta'. Nuestro objetivo es convertir las reseñas de los clientes entre los años 2011 y 2021, en insights accionables que impulsen la excelencia operativa y la satisfacción del cliente en cada local.

## Indicadores claves - KPI’s

- Elevar en un 5% las reseñas positivas respecto al año anterior.

$$
\text{Aumento de reseñas positivas} = \frac{{\text{Número de reseñas positivas en el año actual} - \text{Número de reseñas positivas en el año anterior}}}{{\text{Número de reseñas positivas en el año anterior}}} \times 100
$$

- Mantener una puntuación promedio igual o superior a 3.5 a nivel anual.

$$
\text{Promedio de calificaciones por año} = \frac{\sum_{i=1}^{n} \text{Calificación}_i}{\text{Número total de reseñas en el año}}
$$

- Reducir la tasa de reseñas negativas en un 10% respecto al año anterior.

Tasa de reseñas negativas:

$$
\text{Tasa de reseñas negativas por año} = \frac{{\text{Número de reseñas negativas por año}}}{{\text{Número total de reseñas por año}}} \times 100
$$

Reducción en la tasa de reseñas negativas respecto al año anterior:

$$
\text{Reducción en tasa de reseñas negativas} = \frac{{\text{Tasa de reseñas negativas en el año anterior} - \text{Tasa de reseñas negativas en el año actual}}}{{\text{Tasa de reseñas negativas en el año anterior}}} \times 100
$$

## Objetivos especificos

- Conocer el top 3 de locales con mejores reseñas año a año.
- Evaluar de manera efectiva el desempeño de cada local.
- Identificar áreas de mejora.

## Solución propuesta y entregables

### Dashboard interactivo

- Sedes: Visualiza métricas y análisis por sedes para comparar el rendimiento entre ubicaciones.
- KPI: Destaca indicadores clave de rendimiento (KPI) con métricas anuales asociadas para evaluar el desempeño a lo largo del tiempo.
- Rankings: Muestra varios "Top 3" identificando las mejores y peores sedes en cantidad de reseñas positivas y calificación promedio.

### Modelo predictivo de Machine Learning

Utilizamos el algoritmo SVR (Support Vector Machine for Regression) del modelo Support Vector Machine para predecir el incremento de las calificaciones de las sucursales de McDonald's, en caso de que se realicen mejoras en áreas específicas. El modelo fue entrenado con cada una de las sucursales en un Notebook integrado a Vertex IA, accediendo a los datos limpios almacenados en BigQuery. El modelo entrenado se almaceno en un bucket de Cloud Storage, para su posterior aplicación.

Este modelo fue implementado en un endpoint creado con FastAPI, junto a dos endpoints adicionales que nos ayudarian a dimensionar la situación especifica de cierta sucursal.

<p align='center'> <img src="Img\Esquema ML.jpg" alt="Esquema ML" width="600" height="300" ><p>

#### SentimentAnalysis: 
Este primer endpoint recibe como parametro la *location* de una sucursal, y retorna un diccionario con el total de reseñas, la cantidad de reseñas positivas, neutras y negativas.

#### GetTopWords:
Este segundo endpoint recibe como parametro la *location* de una sucursal, y retorna una nube de palabras con las palabras más frecuentes en las reseñas de baja calificación (menor a 3) para esa sucursal, dandonos una referencia de las áreas a mejorar.

#### PredictScoreIncrement:
Este tercer endpoint recibe como parametro la *location* de una sucursal, y retorna un diccionario con la calificación promedio actual, el incremento de la calificación predicho por el modelo, el porcentaje de ese incremento predicho y la calificación con el incremento sumado.

## Metodologia

Se ha optado por emplear la metodología Scrum, que implica reuniones periódicas de 2 o 3 veces por semana y una comunicación constante a través de plataformas colaborativas. Esto facilita la distribución de tareas y la actualización del estado de las mismas. El proyecto se dividirá en tres Sprints, cada uno con actividades que serán entregadas y revisadas cada 15 días. Posteriormente, estas entregas serán evaluadas para su aprobación o recibirán retroalimentación, según lo determine el Product Owner.

El cronograma para la realización de estas actividades es el que se muestra en la imagen

<p align='center'> <img src="documentación\diagrama de gant.png" width="942" height="452" ><p>

## Equipo de trabajo y roles

| Integrante          | Rol              |
|---------------------|------------------|
| Milagros Torres     | Data Analyst     |
| Rafael Oropeza      | ML Engineer      |
| Dante Chincuini     | Data Engineer    |
| Alejandra Monroy    | Data Analyst     |
| Jonathan Zegarra    | ML Engineer      |

## Stack Tecnológico

<p align='center'> <img src="documentación\stack tecnologico.jpg" width="600" height="300" ><p>

### Python, pandas y numpy

![VSCode](https://img.shields.io/badge/-VSCode-333333?style=flat&logo=visual-studio-code)
![Python](https://img.shields.io/badge/-Python-333333?style=flat&logo=python)
![Jupyter](https://img.shields.io/badge/-Jupyter-333333?style=flat&logo=jupyter)
![Pandas](https://img.shields.io/badge/-Pandas-333333?style=flat&logo=pandas)

Manipulación de datos.

### Google Cloud Plataform

![Google Cloud Plataform](https://img.shields.io/badge/-GoogleCloudPlataform-333333?style=flat&logo=Google-Cloud-Plataform)

Extracción de los datos desde el Data Lake (Cloud Storage) para ser procesados y limpiados a lo largo de la pipeline (Cloud Function) y ser depositados en el Data Warehouse (BigQuery).

### Matplotlib y Seaborn

![Matplotlib](https://img.shields.io/badge/Matplotlib-333333?style=flat&logo=matplotlib)
![Seaborn](https://img.shields.io/badge/Seaborn-333333?style=flat&logo=seaborn)

Creación de gráficos.

### Scikit-learn

![Scikit-learn](https://img.shields.io/badge/Scikitlearn-333333?style=flat&logo=scikitlearn)

Modelo de Machine Learning

### Power BI y Streamlit
![PowerBI](https://img.shields.io/badge/PowerBI-333333?style=flat&logo=powerbi)
![DAX](https://img.shields.io/badge/DAX-333333?style=flat&logo=DAX)
![Streamlit](https://img.shields.io/badge/Streamlit-333333?style=flat&logo=streamlit)

Presentar y disponibilizar los resultados extraídos de los datos de BigQuery.

## Pipeline

<p align='center'> <img src="documentación\ciclo de vida dato.jpeg" width="600" height="300" ><p>

## Análisis Exploratorio de Datos - EDA

Este análisis puede verse de manera detallada en el archivo [EDA.ipynb](https://github.com/DJChincuini/PF_Reviews-Recommendation_Henry/blob/main/EDA.ipynb)

## Diagrama entidad relación 

Diagrama tipo estrella, que cuenta con una tabla central de hechos, la cual es la tabla business y varias tablas de dimensiones en relaciones uno a muchos, que nos amplían el contexto y los detalles de cada sede desde la perspectiva específica de cada dimensión; esto nos permite analizar las métricas por sede.

<p align='center'> <img src="documentación\diagrama ER.PNG" width="600" height="300" ><p>
