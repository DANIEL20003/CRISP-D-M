
# Análisis 1: Resumen de Carga de Datos

**Fecha:** 15 de Enero de 2026

**Autor:** Gemini

## 1. Objetivo

El objetivo de este primer análisis es realizar una carga inicial de los principales conjuntos de datos generados para el proyecto. Se busca verificar que los archivos son accesibles, se pueden cargar en memoria utilizando la librería `pandas` y entender su estructura básica (dimensiones y columnas).

## 2. Proceso

Se ejecutó el script `01_verificar_carga_datos.py`, el cual realiza las siguientes acciones:
1.  Define una lista de los archivos CSV a verificar: `clientes.csv`, `productos.csv`, `ventas.csv` y `detalle_ventas.csv`.
2.  Itera sobre cada archivo, lo carga en un DataFrame de pandas.
3.  Imprime en la consola las dimensiones (número de filas y columnas) y las primeras 5 filas del DataFrame.

## 3. Resultados y Observaciones

A continuación, se presenta un resumen de la estructura de cada archivo cargado.

### a. `clientes.csv`
- **Dimensiones:** 500 filas, 6 columnas.
- **Columnas:** `cliente_id`, `nombre`, `apellido`, `email`, `telefono`, `direccion`.
- **Observación:** El archivo contiene la información demográfica básica de los clientes. El `cliente_id` es la clave primaria. Los datos parecen haber sido generados correctamente.

### b. `productos.csv`
- **Dimensiones:** 150 filas, 6 columnas.
- **Columnas:** `producto_id`, `nombre`, `categoria`, `marca`, `precio_unitario`, `stock`.
- **Observación:** El catálogo de productos está definido en este archivo. `producto_id` es la clave primaria. Se observan diferentes categorías y precios que parecen consistentes con la investigación inicial.

### c. `ventas.csv`
- **Dimensiones:** 1200 filas, 4 columnas.
- **Columnas:** `venta_id`, `fecha`, `cliente_id`, `empleado_id`.
- **Observación:** Este archivo actúa como la tabla maestra de transacciones. Cada fila es una venta única y enlaza al cliente y empleado correspondientes. La columna `fecha` será fundamental para el análisis de Recencia.

### d. `detalle_ventas.csv`
- **Dimensiones:** 3005 filas, 6 columnas.
- **Columnas:** `detalle_id`, `venta_id`, `producto_id`, `cantidad`, `precio_unitario`, `total_linea`.
- **Observación:** Esta es la tabla de detalle. Una sola venta (`venta_id`) puede tener múltiples entradas en este archivo, una por cada producto diferente en la transacción. Las columnas `cantidad` y `total_linea` serán cruciales para calcular el valor Monetario en el análisis RFM.

## 4. Conclusión

Todos los archivos de datos principales se cargaron con éxito. La estructura y el contenido son consistentes con el diseño esperado. No se encontraron errores durante el proceso de carga. El siguiente paso será realizar análisis más profundos sobre cada conjunto de datos para entender las distribuciones y buscar posibles problemas de calidad de datos.
