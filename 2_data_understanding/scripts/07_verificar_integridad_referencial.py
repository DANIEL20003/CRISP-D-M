import pandas as pd
import os

# Define the path to the raw data
DATA_PATH = 'data/raw/'

def verificar_integridad_referencial():
    """
    Verifies referential integrity between key datasets.
    Checks if foreign key values exist in their respective primary key tables.
    """
    print("--- Iniciando Verificación de Integridad Referencial ---\
")

    # --- Load Data ---
    try:
        clientes_df = pd.read_csv(os.path.join(DATA_PATH, 'clientes.csv'))
        productos_df = pd.read_csv(os.path.join(DATA_PATH, 'productos.csv'))
        ventas_df = pd.read_csv(os.path.join(DATA_PATH, 'ventas.csv'))
        detalle_ventas_df = pd.read_csv(os.path.join(DATA_PATH, 'detalle_ventas.csv'))
    except FileNotFoundError as e:
        print(f"Error: Uno o más archivos CSV no encontrados: {e}")
        return
    except Exception as e:
        print(f"Error al cargar los archivos CSV: {e}")
        return

    # --- Extract Primary Keys ---
    pk_clientes = set(clientes_df['cliente_id'])
    pk_productos = set(productos_df['producto_id'])
    pk_ventas = set(ventas_df['venta_id'])

    # --- Define Relationships to Check (Foreign Key -> Primary Key Table) ---
    relationships = {
        'ventas.cliente_id': {'fk_col': 'cliente_id', 'pk_set': pk_clientes, 'pk_name': 'clientes.cliente_id'},
        'ventas.empleado_id': {'fk_col': 'empleado_id', 'pk_set': set(range(1, 26)), 'pk_name': 'empleados.empleado_id (simulado)'}, # Empleados PK was implicit
        'detalle_ventas.venta_id': {'fk_col': 'venta_id', 'pk_set': pk_ventas, 'pk_name': 'ventas.venta_id'},
        'detalle_ventas.producto_id': {'fk_col': 'producto_id', 'pk_set': pk_productos, 'pk_name': 'productos.producto_id'}
    }

    # --- Perform Checks and Report ---
    all_checks_passed = True
    
    # Check ventas.cliente_id
    fk_ventas_clientes = set(ventas_df['cliente_id'])
    orphan_clientes_ventas = fk_ventas_clientes - pk_clientes
    if orphan_clientes_ventas:
        print(f"ALERTA: Se encontraron {len(orphan_clientes_ventas)} 'cliente_id' en 'ventas.csv' que no existen en 'clientes.csv'.")
        # print(f"IDs huérfanos: {list(orphan_clientes_ventas)[:5]}...") # Optional: show some IDs
        all_checks_passed = False
    else:
        print("OK: Todos los 'cliente_id' en 'ventas.csv' tienen una referencia válida en 'clientes.csv'.")

    # Check ventas.empleado_id (against simulated range)
    fk_ventas_empleados = set(ventas_df['empleado_id'])
    orphan_empleados_ventas = fk_ventas_empleados - relationships['ventas.empleado_id']['pk_set']
    if orphan_empleados_ventas:
        print(f"ALERTA: Se encontraron {len(orphan_empleados_ventas)} 'empleado_id' en 'ventas.csv' que no existen en el rango simulado de empleados (1-25).")
        all_checks_passed = False
    else:
        print("OK: Todos los 'empleado_id' en 'ventas.csv' tienen una referencia válida en el rango simulado de empleados.")

    # Check detalle_ventas.venta_id
    fk_detalle_ventas_ventas = set(detalle_ventas_df['venta_id'])
    orphan_ventas_detalle = fk_detalle_ventas_ventas - pk_ventas
    if orphan_ventas_detalle:
        print(f"ALERTA: Se encontraron {len(orphan_ventas_detalle)} 'venta_id' en 'detalle_ventas.csv' que no existen en 'ventas.csv'.")
        all_checks_passed = False
    else:
        print("OK: Todos los 'venta_id' en 'detalle_ventas.csv' tienen una referencia válida en 'ventas.csv'.")

    # Check detalle_ventas.producto_id
    fk_detalle_ventas_productos = set(detalle_ventas_df['producto_id'])
    orphan_productos_detalle = fk_detalle_ventas_productos - pk_productos
    if orphan_productos_detalle:
        print(f"ALERTA: Se encontraron {len(orphan_productos_detalle)} 'producto_id' en 'detalle_ventas.csv' que no existen en 'productos.csv'.")
        all_checks_passed = False
    else:
        print("OK: Todos los 'producto_id' en 'detalle_ventas.csv' tienen una referencia válida en 'productos.csv'.")

    print("\n--- Fin de la Verificación de Integridad Referencial ---")
    if all_checks_passed:
        print("RESUMEN: Todas las verificaciones de integridad referencial pasaron exitosamente. Los datos son consistentes.")
    else:
        print("RESUMEN: Se detectaron problemas de integridad referencial. Se requiere investigación adicional.")

if __name__ == '__main__':
    verificar_integridad_referencial()
