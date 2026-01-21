
# Análisis 6: Reporte de Verificación de Integridad Referencial

**Fecha:** 15 de Enero de 2026

**Autor:** Gemini

## 1. Objetivo

El objetivo de este análisis es verificar la **integridad referencial** entre los diferentes conjuntos de datos (tablas). La integridad referencial asegura que las relaciones entre las tablas son válidas, es decir, que cada "clave foránea" (FK) en una tabla secundaria tiene una correspondiente "clave primaria" (PK) en la tabla principal. Esto es crucial para poder unir las tablas correctamente en la fase de Preparación de Datos y evitar errores o datos inconsistentes en análisis posteriores.

## 2. Concepto de Integridad Referencial

Imagina que tenemos una tabla de `Ventas` y una tabla de `Clientes`. Cada venta en la tabla `Ventas` tiene un `cliente_id` que debería corresponder a un `cliente_id` existente en la tabla `Clientes`. Si una venta tiene un `cliente_id` que no se encuentra en la tabla `Clientes`, esa venta es un registro "huérfano" y se considera un problema de integridad referencial.

Los problemas de integridad referencial pueden llevar a:
-   Uniones de tablas incompletas o incorrectas.
-   Pérdida de datos durante el procesamiento.
-   Resultados de análisis erróneos.
-   Dificultad para construir modelos robustos.

## 3. Proceso

Se ejecutó el script `07_verificar_integridad_referencial.py`, el cual realiza las siguientes comprobaciones:
1.  Carga los archivos `clientes.csv`, `productos.csv`, `ventas.csv` y `detalle_ventas.csv`.
2.  Extrae los conjuntos de claves primarias (`cliente_id`, `producto_id`, `venta_id`) de las tablas principales.
3.  Para cada relación de clave foránea, verifica que todos sus valores existen en el conjunto de claves primarias correspondiente. Las relaciones verificadas fueron:
    -   `ventas.cliente_id` vs `clientes.cliente_id`
    -   `ventas.empleado_id` vs Rango simulado de IDs de empleados (1-25)
    -   `detalle_ventas.venta_id` vs `ventas.venta_id`
    -   `detalle_ventas.producto_id` vs `productos.producto_id`
4.  Reporta cualquier discrepancia encontrada.

## 4. Resultados

Todas las verificaciones de integridad referencial pasaron exitosamente.

-   **`ventas.cliente_id`:** Todos los `cliente_id` en `ventas.csv` tienen una referencia válida en `clientes.csv`.
-   **`ventas.empleado_id`:** Todos los `empleado_id` en `ventas.csv` tienen una referencia válida en el rango simulado de IDs de empleados.
-   **`detalle_ventas.venta_id`:** Todos los `venta_id` en `detalle_ventas.csv` tienen una referencia válida en `ventas.csv`.
-   **`detalle_ventas.producto_id`:** Todos los `producto_id` en `detalle_ventas.csv` tienen una referencia válida en `productos.csv`.

## 5. Conclusión

La verificación de integridad referencial confirma que los conjuntos de datos están bien estructurados y son consistentes entre sí. No se encontraron registros "huérfanos" ni referencias rotas. Esto es fundamental para la fiabilidad de cualquier análisis o modelado futuro, especialmente en la Fase de Preparación de Datos donde estas tablas serán combinadas.

Con este análisis, la Fase 2 (Entendimiento de los Datos) queda completamente finalizada, proporcionando una base sólida y bien comprendida para las siguientes etapas del proyecto CRISP-DM.
