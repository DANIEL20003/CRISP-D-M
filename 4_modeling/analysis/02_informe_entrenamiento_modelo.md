
# Análisis 2: Informe de Entrenamiento del Modelo K-Means

**Fecha:** 15 de Enero de 2026

**Autor:** Gemini

## 1. Objetivo

El objetivo de esta actividad es entrenar el modelo de clustering K-Means final, utilizando el número óptimo de clusters (`k=4`) determinado en el análisis anterior. Además, se busca guardar los artefactos resultantes del entrenamiento para su uso en las fases posteriores del proyecto.

## 2. Proceso

Se ejecutó el script `02_entrenar_modelo_kmeans.py`, que realiza los siguientes pasos:
1.  Carga los datos RFM preparados (`data/processed/rfm_data.csv`).
2.  Estandariza las características RFM.
3.  Inicializa el algoritmo K-Means con el parámetro `n_clusters=4` y una semilla aleatoria (`random_state=42`) para garantizar la reproducibilidad de los resultados.
4.  Entrena el modelo con los datos estandarizados.
5.  Guarda el objeto del modelo entrenado en un archivo.
6.  Asigna la etiqueta del cluster resultante a cada cliente en el conjunto de datos original y guarda este nuevo conjunto de datos.

## 3. Artefactos Generados

El proceso de entrenamiento ha generado dos artefactos clave que son fundamentales para las siguientes fases:

### a. Modelo Entrenado
-   **Archivo:** `models/kmeans_rfm_model.joblib`
-   **Descripción:** Este archivo contiene el modelo K-Means entrenado. Puede ser cargado en el futuro para asignar nuevos clientes a los segmentos existentes sin necesidad de re-entrenar todo el modelo, lo cual es útil para la fase de despliegue.

### b. Datos con Asignación de Clusters
-   **Archivo:** `data/processed/rfm_data_with_clusters.csv`
-   **Descripción:** Este es un archivo CSV que contiene los datos RFM originales junto con una nueva columna llamada `cluster`. Esta columna indica a qué segmento (0, 1, 2 o 3) pertenece cada cliente. Este será el archivo principal para la Fase 5: Evaluación, donde analizaremos el perfil de cada uno de estos segmentos.

## 4. Conclusión

La Fase de Modelado ha concluido exitosamente. Se ha entrenado un modelo de segmentación K-Means y se han generado los artefactos necesarios.

Con el modelo guardado y los clientes etiquetados con sus respectivos segmentos, estamos listos para pasar a la **Fase 5: Evaluación**, donde daremos sentido y valor de negocio a estos grupos.
