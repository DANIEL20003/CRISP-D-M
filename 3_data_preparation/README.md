# Fase 3: Preparación de Datos

En esta fase, se transformarán y limpiarán los datos crudos para construir el conjunto de datos final que se utilizará para el modelado.

## Objetivos Clave (para la Segmentación RFM):
1.  **Unir Datos:** Combinar los datos de `ventas.csv` y `detalle_ventas.csv`.
2.  **Calcular RFM:** Para cada cliente, calcular las métricas de Recencia, Frecuencia y Valor Monetario (RFM).
    - **Recencia:** Tiempo transcurrido desde la última compra.
    - **Frecuencia:** Número total de transacciones.
    - **Monetario:** Gasto total.
3.  **Limpieza y Escalamiento:** Tratar valores atípicos (outliers) si es necesario y escalar las características para que sean comparables por el algoritmo de clustering.
4.  **Exportar Dataset Final:** Guardar la tabla final con los valores RFM por cliente, lista para la fase de modelado.
