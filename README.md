# AirBnB_Ciudad_de_Mexico
 Exploración del alojamiento en Ciudad de Mexico a través de AirBnB.
![Ejemplo de imagen](ejemplo.png)

## Descripción
Como parte de mi transición profesional a Data Analyst, estoy realizando una serie de proyectos en los que pongo en práctica las habilidades y técnicas de análisis de datos adquiridas 📊

En este post os comparto mi último proyecto, orientado a analizar el mercado de Airbnb en la Ciudad de México.

Airbnb ha transformado la vida de nuestras ciudades desde su irrupción en 2007. En México, las pernoctaciones extrahoteleras como las de Airbnb aumentaron un 50,7% para el conjunto del año 2023 y alcanzaron las cifras de 2019, según datos del INEGI (2023) 📈

En este proyecto analizo el mercado de Airbnb en la Ciudad de México con datos actualizados a febrero de 2024. A nivel técnico, consultas a la base de datos y, una vez obtenidos los principales indicadores, conecté los datos y creé las visualizaciones usando Power BI 📶

Mis principales conclusiones sobre el mercado de Airbnb en la Ciudad de México:

- La Ciudad de México ofrece 22962 alojamientos de Airbnb, gestionados por 10609 propietarios.
- El mercado de Airbnb en la Ciudad de México tiene una fuerte tendencia a la concentración. Un 1% de propietarios gestiona el 20% de los alojamientos. Así 100 propietarios concentran la oferta de casi 4500 alojamientos.
- La alcaldía Cuauhtémoc, una de las más céntricas de la ciudad, es la de mayor concentración de inmuebles, representando aproximadamente el 45 % del total de alojamientos ofertados.
- El precio medio de un Airbnb en la Ciudad de México es de 412 pesos mexicanos.
- El alojamiento entero es la tipología de alojamiento más ofertada. Un 64% de los alojamientos ofertados son de viviendas enteras, frente a un 34% de habitaciones privadas.
- El precio medio de un alojamiento entero es de 1350 pesos mexicanos.
- Las alcaldías con mayor número de reseñas son: Cuauhtémoc, Miguel Hidalgo y Benito Juarez.

## Proceso de Análisis de Datos y Regresión para Airbnb

### Importar Datos:
Para importar los datos, podemos utilizar la sección "Get the data" del sitio web Inside Airbnb. Puedes acceder a esta sección en el siguiente enlace: [Inside Airbnb - Get the data](http://insideairbnb.com/get-the-data.html).

Dentro de esta página, encontrarás una lista de ciudades donde Airbnb está disponible. Puedes seleccionar la Ciudad de México y descargar el conjunto de datos más reciente disponible. Una vez descargado, puedes proceder a cargar los datos en tu entorno de desarrollo para comenzar el análisis.

### Tratamiento de Datos:
1. Comprobación de valores nulos y eliminación o imputación de los mismos.
2. Identificación y eliminación de valores duplicados.
3. Agrupación de variables categóricas y generación de nuevas columnas.
4. Estimación de variables faltantes utilizando técnicas como la imputación basada en el promedio, mediana o regresión lineal múltiple.
5. Escalado de variables numéricas si es necesario para modelos de aprendizaje automático.

### Análisis Exploratorio:
1. Carga de los datos: Se cargan los datos desde el archivo 'datos_limpios_airbnb.csv' utilizando Pandas.
2. Rellenar datos nulos: Se rellenan los valores nulos en el DataFrame utilizando la media para columnas numéricas y la moda para columnas categóricas.
3. Distribución de las variables: Se visualiza la distribución de las variables numéricas utilizando histogramas.
4. Descripción de las variables: Se proporciona una descripción estadística de todas las variables del DataFrame.
5. Evaluación de la asimetría: Se calcula la asimetría (skewness) de cada variable numérica en el DataFrame.
6. Detección de outliers: Se identifican los valores atípicos (outliers) en cada columna del DataFrame utilizando el método del rango intercuartílico (IQR).
7. Reemplazo de outliers mediante Isolation Forest: Se define una función para reemplazar los outliers utilizando el algoritmo de Isolation Forest.
8. Matriz de correlación por Spearman: Se visualiza la matriz de correlación de las variables utilizando el coeficiente de correlación de Spearman.
9. Normalizar variables con Min Max Scaler: Se normalizan las variables numéricas utilizando Min Max Scaler.
10. Elección de variables con mayor correlación: Se identifican las variables que tienen una correlación alta con la variable objetivo utilizando un umbral de correlación.
11. Crear un DataFrame con variables de alta correlación: Se crea un nuevo DataFrame que incluye solo las variables con alta correlación con la variable objetivo.
12. Guardar datos como CSV: Se guarda el DataFrame resultante como un archivo CSV llamado 'datos_limpios_airbnb_alta_correlacion.csv'.

### Regresión:
1. División del conjunto de datos en conjuntos de entrenamiento y prueba.
2. Selección de variables relevantes para el modelo de regresión lineal múltiple.
3. Entrenamiento del modelo de regresión lineal múltiple.
4. Ajuste y evaluación del modelo utilizando métricas como RMSE, varianza explicada y R².
5. Optimización del modelo si es necesario, ajustando hiperparámetros o realizando selección de variables.
6. Predicción del precio promedio de alojamientos en el conjunto de prueba.
7. Evaluación de la precisión de la predicción utilizando métricas como RMSE, varianza explicada y R².
8. Utilización del modelo para predecir precios promedio en nuevos casos.

## Archivos Contenidos
- Jupyter Notebook con el procesamiento de datos.
- Aplicación Python para la predicción del precio por noche en euros.
- Paneles interactivos de Power BI.
                Enlaces: HTML :"<iframe title="ciudad_de_mexico_airbnb" width="600" height="373.5" src="https://app.powerbi.com/view?r=eyJrIjoiZTg1NmQ1MjQtYTM0NS00NzgxLWFkZjQtZmMwY2ZkYmYwOWJlIiwidCI6IjhhZWJkZGI2LTM0MTgtNDNhMS1hMjU1LWI5NjQxODZlY2M2NCIsImMiOjl9" frameborder="0" allowFullScreen="true"></iframe>"
                         URL: "https://app.powerbi.com/view?r=eyJrIjoiZTg1NmQ1MjQtYTM0NS00NzgxLWFkZjQtZmMwY2ZkYmYwOWJlIiwidCI6IjhhZWJkZGI2LTM0MTgtNDNhMS1hMjU1LWI5NjQxODZlY2M2NCIsImMiOjl9"

  
¡Espero que encuentres útil este proyecto y los insights proporcionados! Si tienes alguna pregunta o sugerencia, ¡no dudes en contactarme!
```
