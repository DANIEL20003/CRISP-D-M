import pandas as pd
import os

# Define the path to the raw data
DATA_PATH = 'data/raw/'

# List of files to check
files_to_check = ['clientes.csv', 'productos.csv', 'ventas.csv', 'detalle_ventas.csv']

def verificar_carga_datos():
    """
    Loads the main CSV files, prints their shape and the first 5 rows.
    """
    print("--- Iniciando Verificación de Carga de Datos ---\
")
    
    for file_name in files_to_check:
        file_path = os.path.join(DATA_PATH, file_name)
        
        if not os.path.exists(file_path):
            print(f"** Archivo no encontrado: {file_path} **\
")
            continue
            
        print(f"--- Cargando archivo: {file_name} ---")
        
        try:
            df = pd.read_csv(file_path)
            
            print(f"Dimensiones: {df.shape[0]} filas, {df.shape[1]} columnas")
            print("Primeras 5 filas:")
            print(df.head())
            print("\n" + "="*50 + "\n")
            
        except Exception as e:
            print(f"** Error al cargar o procesar el archivo {file_name}: {e} **\
")

if __name__ == '__main__':
    verificar_carga_datos()
