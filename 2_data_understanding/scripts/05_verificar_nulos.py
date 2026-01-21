import pandas as pd
import os

# Define the path to the raw data
DATA_PATH = 'data/raw/'

# List of files to check, focusing on those for RFM analysis
files_to_check = ['clientes.csv', 'ventas.csv', 'detalle_ventas.csv', 'productos.csv']

def verificar_nulos():
    """
    Loads key CSV files and checks for missing values in each column.
    """
    print("--- Iniciando Verificación de Valores Nulos ---")
    
    for file_name in files_to_check:
        file_path = os.path.join(DATA_PATH, file_name)
        
        if not os.path.exists(file_path):
            print(f"** Archivo no encontrado: {file_path} **")
            continue
            
        print(f"--- Revisando archivo: {file_name} ---")
        
        try:
            df = pd.read_csv(file_path)
            
            null_counts = df.isnull().sum()
            
            if null_counts.sum() == 0:
                print("No se encontraron valores nulos en ninguna columna.")
            else:
                print("Recuento de valores nulos por columna:")
                print(null_counts[null_counts > 0])
            
            print("\n" + "="*50 + "\n")
            
        except Exception as e:
            print(f"** Error al cargar o procesar el archivo {file_name}: {e} **")

if __name__ == '__main__':
    verificar_nulos()
