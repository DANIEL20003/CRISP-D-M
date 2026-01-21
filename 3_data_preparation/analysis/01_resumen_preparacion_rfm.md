
# Análisis 1: Resumen de Preparación de Datos RFM

**Fecha:** 15 de Enero de 2026

**Autor:** Gemini

## 1. Objetivo
El objetivo de la Fase de Preparación de Datos fue transformar los datos transaccionales crudos (`ventas.csv` y `detalle_ventas.csv`) en un conjunto de datos agregado y significativo, listo para el modelado de segmentación. Este conjunto de datos se basa en el modelo **RFM (Recencia, Frecuencia, Monetario)**.

## 2. Definición de las Métricas RFM

-   **Recencia (Recency):** ¿Qué tan recientemente ha comprado un cliente? Se mide como el número de días entre la última compra del cliente y una fecha de referencia fija ("snapshot date"). Un valor bajo es mejor (cliente más reciente).
-   **Frecuencia (Frequency):** ¿Con qué frecuencia compra un cliente? Se mide como el número total de transacciones únicas que ha realizado el cliente. Un valor alto es mejor.
-   **Valor Monetario (Monetary):** ¿Cuánto dinero ha gastado un cliente? Se mide como la suma total del dinero gastado por el cliente en todas sus compras. Un valor alto es mejor.

## 3. Proceso de Preparación

Se ejecutó el script `01_calcular_rfm.py`, que realizó los siguientes pasos:
1.  Cargó los datos de ventas y detalles de venta.
2.  Unió ambas tablas para tener el valor monetario en cada transacción.
3.  Calculó una "snapshot date" (el día después de la última transacción registrada en todo el dataset) para asegurar que la Recencia se mida de manera consistente para todos los clientes.
4.  Agrupó todos los registros por `cliente_id`.
5.  Para cada cliente, calculó las métricas R, F y M.
6.  Guardó el nuevo conjunto de datos en `data/processed/rfm_final_data.csv`.

## 4. Resumen del Dataset Resultante

El dataset final contiene el `cliente_id` como índice y las tres nuevas características.

**Primeras 5 Filas:**
```
| cliente_id | recency | frequency | monetary |
|-----------:|--------:|----------:|---------:|
|          1 |     321 |         2 |  3981.82 |
|          2 |     458 |         1 |  3987.97 |
|          3 |     190 |         4 |  1716.29 |
|          4 |     153 |         3 |  5350.56 |
|          5 |      34 |         1 |   374.02 |
```

**Estadísticas Descriptivas de las Características RFM:**
```
|         |   recency |   frequency |    monetary |
|:--------|----------:|------------:|------------:|
| count   |  473      |    473      |     473     |
| mean    |  356.5    |      2.53   |    3636.5   |
| std     |  282.83   |      1.42   |    3203.49  |
| min     |    1      |      1      |     109.91  |
| 25%     |  112      |      1      |    1198.81  |
| 50%     |  319      |      2      |    2831.67  |
| 75%     |  565      |      3      |    5142.13  |
| max     | 1095      |      9      |   22964.6   |
```

**Observaciones:**
- De los 500 clientes originales, 473 han realizado al menos una compra.
- La `recency` varía desde 1 día hasta casi 3 años (1095 días).
- La `frequency` media es de ~2.5 compras por cliente, con un máximo de 9.
- El `monetary` muestra una gran dispersión, con un valor medio de ~$3636 y un máximo de ~$22964, lo que confirma la asimetría que vimos en la Fase 2.

## 5. Conclusión
La Fase 3 ha concluido exitosamente. Se ha generado un conjunto de datos limpio y agregado que captura el comportamiento de compra de cada cliente a través de las métricas RFM. Este archivo (`rfm_final_data.csv`) es el input directo para la Fase 4: Modelado.
