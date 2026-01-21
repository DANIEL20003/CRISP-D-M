# Fase 4: Modelado

En esta fase, se aplicarán técnicas de modelado para lograr los objetivos de minería de datos definidos en el `project_charter.md`.

## Objetivos Clave (para la Segmentación RFM):
1.  **Seleccionar Algoritmo:** Se utilizará el algoritmo de clustering **K-Means**, que es apropiado para la segmentación de clientes.
2.  **Determinar Número Óptimo de Clusters (K):** Aplicar técnicas como el "Método del Codo" (Elbow Method) y el "Coeficiente de Silueta" para encontrar el número ideal de segmentos de clientes.
3.  **Entrenar el Modelo:** Ejecutar el algoritmo K-Means sobre el conjunto de datos RFM preparado.
4.  **Asignar Segmentos:** Asignar a cada cliente su etiqueta de segmento correspondiente.
5.  **Guardar el Modelo:** Serializar y guardar el modelo de clustering entrenado para su uso futuro en la fase de evaluación o despliegue.
