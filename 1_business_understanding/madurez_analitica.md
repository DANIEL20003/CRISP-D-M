
# Evaluación de Madurez Analítica: "ElectroHogar Riobamba"

**Fecha de Evaluación:** 15 de Enero de 2026

## Resumen Ejecutivo

La madurez analítica de "ElectroHogar Riobamba" se encuentra en una etapa **"Principiante" / "Descriptiva"**. La empresa ha comenzado a recolectar datos de manera estructurada gracias a su sistema ERP, pero el uso de estos datos para la toma de decisiones estratégicas es todavía limitado y, en su mayoría, reactivo. Los análisis se centran en describir lo que ha sucedido en el pasado en lugar de predecir tendencias futuras o prescribir acciones.

## Dimensiones de Madurez Analítica

### 1. Datos
- **Nivel: Básico**
- **Recolección:** La principal fuente de datos es el ERP, que captura información de ventas, inventario y clientes. Los datos son estructurados y de calidad aceptable para análisis básicos.
- **Accesibilidad:** El acceso a los datos está centralizado en el gerente de la tienda y un asistente administrativo, quienes pueden generar reportes desde el ERP.
- **Integración:** No se integran fuentes de datos externas (ej. datos de redes sociales, análisis web, datos demográficos de mercado) con los datos del ERP.

### 2. Herramientas y Tecnología
- **Nivel: Básico**
- **Software:** La herramienta principal es el propio módulo de reportería del ERP. Ocasionalmente se utiliza Microsoft Excel para análisis manuales y la creación de gráficos simples.
- **Infraestructura:** No existe un almacén de datos (data warehouse) o un lago de datos (data lake). Todos los análisis se ejecutan directamente sobre la base de datos transaccional del ERP, lo que puede limitar la complejidad de las consultas.
- **Visualización:** Se utilizan tablas y gráficos básicos generados por el ERP o Excel. No se emplean herramientas de Business Intelligence (BI) como Power BI, Tableau o Looker.

### 3. Análisis
- **Nivel: Descriptivo**
- **Tipo de Análisis:** El enfoque es 100% en la **analítica descriptiva**. Se generan reportes para responder preguntas como:
    - ¿Cuál fue el total de ventas del mes pasado?
    - ¿Qué productos son los más vendidos?
    - ¿Qué vendedor generó más ventas?
- **Capacidades:** No se aplican técnicas de **analítica diagnóstica** (¿por qué cayeron las ventas?), **predictiva** (¿cuál será nuestra demanda el próximo trimestre?) o **prescriptiva** (¿qué oferta debemos hacer a este cliente para maximizar la probabilidad de compra?).

### 4. Gobernanza y Talento
- **Nivel: Principiante**
- **Roles:** No existe un rol dedicado a la analítica de datos. Las tareas de reportería son una función secundaria del personal administrativo.
- **Cultura de Datos:** La toma de decisiones se basa fuertemente en la experiencia y la intuición de la gerencia, complementada por los reportes de ventas básicos. No hay una cultura generalizada de "tomar decisiones basadas en datos".
- **Gobernanza:** No hay políticas formales de gobernanza de datos, calidad de datos o seguridad más allá de las que provee el sistema ERP.

## Recomendaciones y Próximos Pasos

1.  **Desarrollar Capacidades en BI:** Adoptar una herramienta de Business Intelligence (como Power BI, que tiene una barrera de entrada baja) para conectar al ERP. Esto permitiría crear dashboards interactivos y visualizaciones más ricas que los reportes estáticos actuales.
2.  **Iniciar con Analítica Diagnóstica:** Fomentar que el equipo directivo empiece a cruzar datos para responder preguntas de "por qué". Por ejemplo:
    - Comparar ventas de un producto vs. campañas en redes sociales.
    - Analizar la estacionalidad de las ventas por categoría de producto.
    - Segmentar clientes por frecuencia y valor de compra (Análisis RFM básico).
3.  **Capacitación en Análisis de Datos:** Ofrecer formación básica al personal clave (gerencia, administración) en fundamentos de análisis de datos y uso de la herramienta de BI seleccionada.
4.  **Proyecto Piloto Predictivo:** Como un objetivo a mediano plazo (1-2 años), plantear un proyecto piloto simple de analítica predictiva, como un **pronóstico de demanda** para las categorías de productos más importantes, utilizando los datos históricos de ventas. Esto sentaría las bases para optimizar el inventario.
