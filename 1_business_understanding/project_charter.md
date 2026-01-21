
# Project Charter: Mejora de la Estrategia Comercial de ElectroHogar Riobamba

**Fecha:** 15 de Enero de 2026

## 1. Antecedentes y Contexto

ElectroHogar Riobamba es una empresa consolidada con 20 años en el mercado local de electrodomésticos. La compañía se encuentra en una fase inicial de transformación digital y analítica ("Competente Digital" y "Analítica Descriptiva"). Actualmente, sus operaciones se apoyan en un sistema ERP, pero la toma de decisiones estratégicas se basa más en la experiencia que en el análisis de datos profundo.

Existe una oportunidad significativa para aprovechar los datos de ventas históricos y de clientes para pasar de una estrategia reactiva a una proactiva, mejorando la eficiencia del marketing y la gestión de inventario.

## 2. Objetivos de Negocio

Para el próximo ciclo de 12 meses, la empresa se plantea los siguientes objetivos de negocio medibles:

1.  **Aumentar las Ventas Cruzadas (Cross-selling):** Incrementar en un 15% las ventas de productos complementarios a los clientes existentes.
2.  **Optimizar la Gestión de Inventario:** Reducir en un 20% los costos asociados al exceso de stock en categorías de baja rotación.
3.  **Incrementar la Retención de Clientes:** Mejorar la tasa de recompra de clientes en un 10%.

## 3. Objetivos de Minería de Datos

Para apoyar la consecución de los objetivos de negocio, se definen los siguientes objetivos técnicos de minería de datos:

1.  **Análisis de la Cesta de Compra (Market Basket Analysis):**
    - **Objetivo:** Identificar patrones de compra y descubrir qué productos se compran juntos con frecuencia.
    - **Relación con Negocio:** Este análisis proporcionará la base para crear promociones de "combos" y estrategias de venta cruzada (Objetivo de Negocio 1).

2.  **Pronóstico de Demanda (Demand Forecasting):**
    - **Objetivo:** Desarrollar un modelo que prediga las ventas mensuales para las principales categorías de productos.
    - **Relación con Negocio:** Un pronóstico preciso permitirá ajustar las compras a proveedores, optimizando los niveles de stock y reduciendo el capital inmovilizado (Objetivo de Negocio 2).

3.  **Segmentación de Clientes (Customer Segmentation - RFM):**
    - **Objetivo:** Clasificar a los clientes en segmentos basados en su comportamiento de compra (Recencia, Frecuencia, Valor Monetario).
    - **Relación con Negocio:** Permitirá identificar a los clientes más valiosos, los clientes en riesgo y los nuevos clientes, para diseñar campañas de marketing personalizadas y mejorar la retención (Objetivo de Negocio 3).

## 4. Plan del Proyecto (Foco Inicial: Segmentación de Clientes)

Se propone abordar estos objetivos de forma secuencial. El primer proyecto se centrará en la **Segmentación de Clientes (RFM)** por su alto impacto potencial y complejidad manejable.

- **Fase 2: Data Understanding:** Explorar los datos de `clientes.csv` y `ventas.csv` para analizar la distribución de compras y la calidad de los datos.
- **Fase 3: Data Preparation:** Calcular los valores de Recencia, Frecuencia y Monetario para cada cliente. Limpiar y transformar los datos para el modelado.
- **Fase 4: Modeling:** Aplicar algoritmos de clustering (ej. K-Means) para agrupar a los clientes en distintos segmentos.
- **Fase 5: Evaluation:** Evaluar la calidad de los segmentos (ej. con el coeficiente de silueta) y describir las características de cada uno (ej. "Campeones", "En Riesgo", "Nuevos").
- **Fase 6: Deployment:** Entregar un informe con la descripción de cada segmento y una lista de clientes por segmento. Diseñar un plan de acción de marketing para cada uno.

## 5. Criterios de Éxito

### Criterios de Éxito del Negocio
- Se alcanza el objetivo de aumentar la tasa de recompra en un 10% después de 6 meses de aplicar las campañas dirigidas a los segmentos identificados.
- El costo de adquisición de clientes se reduce en un 5% gracias a campañas más efectivas.

### Criterios de Éxito de Minería de Datos (para la Segmentación RFM)
- El modelo de clustering K-Means produce 3-5 segmentos de clientes claramente diferenciados.
- El modelo alcanza un coeficiente de silueta superior a 0.5, indicando una buena separación entre clusters.
- El informe final es claro y accionable para el equipo de marketing y ventas.
