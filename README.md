<h1 align="center"><b>Proyecto de Análisis y Machine Learning McDonald's</b></h1>

## Contexto

McDonald's, una de las principales empresas de comida rápida a nivel global, está implementando un sistema de incentivos para sus empleados en el estado Florida como parte de su compromiso continuo con la mejora del servicio al cliente. Este piloto no solo reconoce el desempeño excepcional del equipo, sino que también busca evaluar la efectividad del sistema en un entorno operativo real. McDonald's espera que estos incentivos fortalezcan su posición como líder en la industria y mejoren la experiencia del cliente en sus locales del estado Florida y más allá.

## Estructura

El presente proyecto cuuenta con las siguientes carpetas y archivos:

- [Datos](https://github.com/DJChincuini/PF_Reviews-Recommendation_Henry/tree/main/Datos): Contiene archivos en formato .parquet filtrados por los datos de interes utilizados para la realización del EDA.
- [ETL](https://github.com/DJChincuini/PF_Reviews-Recommendation_Henry/tree/main/ETL): Contiene los archivos utilizados para la realización del ETL de manera local.
- [Img](https://github.com/DJChincuini/PF_Reviews-Recommendation_Henry/tree/main/Img): Contiene imagenes utilizadas durante el desarrollo del proyecto.

## ¿Quienes somos?

En Data Feedback Solutions somos tu aliado estratégico, dedicados a convertir la opinión de tus clientes en datos valiosos. Nuestro objetivo es llevar tu negocio al siguiente nivel, proporcionándote insights precisos y relevantes para impulsar tu éxito.

## Objetivo general y alcance

Data Feedback Solutions ha sido contratada por McDonald's con el objetivo de mejorar el rendimiento de sus locales en el estado de Florida y asegurar que cada visita sea una experiencia que haga decir 'Me encanta'. Nuestro objetivo es convertir las reseñas de los clientes entre los años 2010  y 2022, en insights accionables que impulsen la excelencia operativa y la satisfacción del cliente en cada local.

## Indicadores claves - KPI’s

- Elevar en un 5% las reseñas positivas respecto al año anterior.

$$
\text{Aumento de reseñas positivas} = \frac{{\text{Número de reseñas positivas en el año actual} - \text{Número de reseñas positivas en el año anterior}}}{{\text{Número de reseñas positivas en el año anterior}}} \times 100
$$

- Mantener una puntuación promedio igual o superior a 4 a nivel anual.

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

### Sistema de recomendación

Una API, con las siguientes 4 funciones

- Top 3 locales con mayor cantidad de reseñas positivas: recibe como input el año en formato AAAA y devuelve el top 3 de locales con mayor cantidad de reseñas positivas en el estado de Florida para el año ingresado con la siguiente información, ubicación del local, cantidad de reseñas positivas y ciudad.
- Top 3 de locales con mejor puntuación promedio por año: recibe como imput una ciudad y devuelve el top 3 de locales con mejor calificación promedio por año para la ciudad ingresada con la siguiente infomación año, ubicación del local y puntuación promedio.
- Top 3 de locales con peor puntuación promedio por año: recibe como imput una ciudad y devuelve el top 3 de locales con peor calificación promedio por año para la ciudad ingresada con la siguiente infomación año, ubicación del local y puntuación promedio.
- Top 3 de locales con menor porcentaje de reseñas negativas en el estado de Florida: recibe como input el año en formato AAAA y devuelve el top 3 de locales con menor porcentaje de reseñas negativas en el estado de Florida para el año ingresado con la siguiente información, ubicación del local, porcentaje de reseñas negativas y ciudad.

### Análisis de sentimiento

Palabras Clave por Sentimiento: Identificación de las palabras más frecuentes en reseñas positivas y negativas para comprender qué aspectos son más valorados por los clientes y cuáles son problemáticos.

## Metodologia

Se ha optado por emplear la metodología Scrum, que implica reuniones periódicas de 2 o 3 veces por semana y una comunicación constante a través de plataformas colaborativas. Esto facilita la distribución de tareas y la actualización del estado de las mismas. El proyecto se dividirá en tres Sprints, cada uno con actividades que serán entregadas y revisadas cada 15 días. Posteriormente, estas entregas serán evaluadas para su aprobación o recibirán retroalimentación, según lo determine el Product Owner.

El cronograma para la realización de estas actividades es el que se muestra en la imagen
