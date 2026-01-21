# Análisis de Capacidad del Sistema

**Fecha:** 15 de Enero de 2026

## 1. Objetivo
Atendiendo a la solicitud, se ha realizado una comprobación de los recursos de hardware de la máquina actual para determinar su suficiencia para el procesamiento requerido por este proyecto de minería de datos.

## 2. Especificaciones del Sistema
Se obtuvieron las siguientes especificaciones a través de los comandos del sistema operativo:

-   **Procesador:** 12th Gen Intel(R) Core(TM) i3-1215U
-   **Memoria Física Total:** 16,070 MB (~16 GB)
-   **Memoria Física Disponible:** 3,790 MB (~3.8 GB)

## 3. Conclusión
La capacidad de esta máquina **es más que suficiente** para las tareas de este proyecto.

### Justificación:
1.  **Tamaño de los Datos:** Los conjuntos de datos que hemos generado son pequeños (< 5 MB en total) y caben cómodamente en la memoria RAM disponible.
2.  **Complejidad del Algoritmo:** El algoritmo K-Means es computacionalmente eficiente. El entrenamiento del modelo sobre nuestro conjunto de datos se completa en cuestión de segundos.
3.  **Escalabilidad Futura:** Si en el futuro los datos crecieran significativamente (millones de registros), la memoria RAM disponible (~16 GB) seguiría siendo adecuada para muchas tareas de análisis de datos con `pandas` y `scikit-learn` antes de necesitar recurrir a técnicas más avanzadas como el procesamiento en lotes (batch processing) o herramientas de big data (como Spark).

No se prevén cuellos de botella de rendimiento con la configuración actual del hardware para los objetivos definidos en este proyecto.
