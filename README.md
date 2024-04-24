![Portada](https://i.imgur.com/hFWnAnb.jpeg)

<h1 align="center"><b>Proyecto de Análisis de Datos y Machine Learning McDonald's</b></h1>

## Contexto

McDonald's, una de las principales empresas de comida rápida a nivel global, está implementando un sistema de incentivos para sus empleados en el estado Florida como parte de su compromiso continuo con la mejora del servicio al cliente. Este piloto no solo reconoce el desempeño excepcional del equipo, sino que también busca evaluar la efectividad del sistema en un entorno operativo real. McDonald's espera que estos incentivos fortalezcan su posición como líder en la industria y mejoren la experiencia del cliente en sus locales del estado Florida y más allá.

<p align='center'> <img src="Img\Img-Mc.jpg" alt="Accidente vial" width="800" height="300" ><p>

## Estructura

El presente proyecto cuuenta con las siguientes carpetas y archivos:

- [Datos](https://github.com/DJChincuini/PF_Reviews-Recommendation_Henry/tree/main/Datos): Contiene archivos en formato .parquet filtrados por los datos de interes utilizados para la realización del EDA.
- [ETL](https://github.com/DJChincuini/PF_Reviews-Recommendation_Henry/tree/main/ETL): Contiene los archivos utilizados para la realización del ETL de manera local.
- [Img](https://github.com/DJChincuini/PF_Reviews-Recommendation_Henry/tree/main/Img): Contiene imagenes utilizadas durante el desarrollo del proyecto.
- [Documentación](https://github.com/DJChincuini/PF_Reviews-Recommendation_Henry/tree/main/documentaci%C3%B3n): Contiene la documentación generada durante la realización del proyecto.
- [_pycache_](https://github.com/DJChincuini/PF_Reviews-Recommendation_Henry/tree/main/__pycache__): Contine archivos de caché que contienen código compilado en formato bytecode. Estos archivos se generan automáticamente por el intérprete de Python.

## ¿Quienes somos?

En Data Feedback Solutions somos tu aliado estratégico, dedicados a convertir la opinión de tus clientes en datos valiosos. Nuestro objetivo es llevar tu negocio al siguiente nivel, proporcionándote insights precisos y relevantes para impulsar tu éxito.

<p align='center'> <img src="Img\logo.jpg" alt="Accidente vial" width="300" height="300" ><p>

## Objetivo general y alcance

Data Feedback Solutions ha sido contratada por McDonald's con el objetivo de mejorar el rendimiento de sus locales en el estado de Florida y asegurar que cada visita sea una experiencia que haga decir 'Me encanta'. Nuestro objetivo es convertir las reseñas de los clientes entre los años 2010  y 2022, en insights accionables que impulsen la excelencia operativa y la satisfacción del cliente en cada local.

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

### Sistema de recomendación

Una API, con las siguientes 3 funciones

En proceso

### Análisis de sentimiento

Palabras Clave por Sentimiento: Identificación de las palabras más frecuentes en reseñas positivas y negativas para comprender qué aspectos son más valorados por los clientes y cuáles son problemáticos.

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

Manipulación de datos.

### Google Cloud Platafform

Extracción, transformación y manipulación de todos los conjuntos de datos. Disponibilización en la nube.

### Matplotlib y Seaborn

Creación de gráficos.

### Scikit-learn

Análisis de sentimiento

### Power BI y Streamlit

Presentar y disponibilizar los resultados.

## Pipeline

<p align='center'> <img src="documentación\ciclo de vida dato.jpeg" alt="Accidente vial" width="600" height="300" ><p>

## Análisis Exploratorio de Datos - EDA

Este análisis puede verse de manera detallada en el archivo [EDA.ipynb](https://github.com/DJChincuini/PF_Reviews-Recommendation_Henry/blob/main/EDA.ipynb)
