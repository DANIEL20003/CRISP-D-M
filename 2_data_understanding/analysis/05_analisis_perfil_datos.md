
# Análisis 5: Análisis de Perfil Automatizado de Datos

**Fecha:** 15 de Enero de 2026

**Autor:** Gemini

## 1. Objetivo

Para enriquecer la fase de Entendimiento de los Datos, se realiza un análisis de perfilado automático utilizando la librería `ydata-profiling`. El objetivo es generar un informe exhaustivo y detallado de cada conjunto de datos clave para obtener una comprensión profunda de las variables, sus distribuciones, interacciones y posibles problemas de calidad de forma rápida y eficiente.

## 2. Proceso

Se ejecutó el script `06_generar_reporte_perfil_datos.py`, que realiza los siguientes pasos:
1.  Define una lista de los archivos a analizar: `clientes.csv`, `productos.csv` y `ventas.csv`.
2.  Para cada archivo, lo carga en un DataFrame de pandas.
3.  Utiliza la función `ProfileReport` de `ydata-profiling` para crear un análisis completo.
4.  Guarda el informe resultante como un archivo HTML interactivo en la carpeta `2_data_understanding/plots/`.

## 3. Resultados e Informes

Se generaron tres informes interactivos, uno para cada conjunto de datos. Estos informes contienen un análisis detallado que incluye:
-   **Visión General (Overview):** Estadísticas generales, número de variables, observaciones, valores faltantes, etc.
-   **Análisis por Variable:** Un análisis en profundidad para cada columna, incluyendo estadísticas descriptivas y un gráfico de distribución.
-   **Correlaciones:** Matrices de correlación (ej. de Pearson, Spearman) para identificar relaciones entre variables numéricas.
-   **Alertas:** Advertencias sobre problemas potenciales como alta cardinalidad, asimetría, ceros, etc.

### Informes Generados:
*   **[Reporte de Perfil de `clientes.csv`](../plots/perfil_clientes.html)**
*   **[Reporte de Perfil de `productos.csv`](../plots/perfil_productos.html)**
*   **[Reporte de Perfil de `ventas.csv`](../plots/perfil_ventas.html)**

*(Nota: Para ver los informes, abre los archivos HTML en un navegador web.)*

### Principales Hallazgos (Resumen):
- **Confirmación de Calidad:** Los informes confirman los hallazgos de los análisis anteriores: no hay valores faltantes.
- **Tipos de Datos:** Los tipos de datos inferidos por la librería son correctos en su mayoría (numéricos, categóricos, etc.). En `ventas.csv`, la columna `fecha` fue correctamente identificada como tipo fecha.
- **Alertas de Cardinalidad:** En `clientes.csv`, las variables como `nombre`, `email`, y `telefono` tienen una alta cardinalidad (muchos valores únicos), lo cual es esperado. Esto simplemente confirma que son identificadores únicos.
- **Distribuciones:** Los informes proporcionan histogramas interactivos para todas las variables numéricas, confirmando visualmente las distribuciones que analizamos en los pasos anteriores (ej. la asimetría en `precio_unitario` en el informe de productos).

## 4. Conclusión

El uso de `ydata-profiling` ha acelerado y profundizado enormemente la fase de Entendimiento de los Datos. En cuestión de minutos, hemos generado un análisis completo que habría llevado horas realizar manualmente.

Estos informes sirven como una "hoja de datos" (datasheet) viva para nuestros conjuntos de datos, y serán una referencia valiosa en las fases posteriores del proyecto. Con este análisis exhaustivo, podemos concluir la Fase 2 con un alto grado de confianza en nuestra comprensión de los datos disponibles.
