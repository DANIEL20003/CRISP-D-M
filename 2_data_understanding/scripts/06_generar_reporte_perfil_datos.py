import pandas as pd
from ydata_profiling import ProfileReport
import os

# Define paths
DATA_PATH = 'data/raw/'
REPORT_PATH = '2_data_understanding/plots/' # Saving HTML reports in the 'plots' folder for consistency

# List of files to profile
files_to_profile = {
    'clientes.csv': 'perfil_clientes.html',
    'productos.csv': 'perfil_productos.html',
    'ventas.csv': 'perfil_ventas.html',
}

def generar_reporte_perfil_datos():
    """
    Generates a detailed data profile report for key CSV files using ydata-profiling.
    """
    print("--- Iniciando Generación de Reportes de Perfil de Datos ---\
")
    
    if not os.path.exists(REPORT_PATH):
        os.makedirs(REPORT_PATH)

    for file_name, report_name in files_to_profile.items():
        file_path = os.path.join(DATA_PATH, file_name)
        report_path = os.path.join(REPORT_PATH, report_name)
        
        if not os.path.exists(file_path):
            print(f"** Archivo no encontrado: {file_path} **\
")
            continue
            
        print(f"--- Generando reporte para: {file_name} ---")
        
        try:
            df = pd.read_csv(file_path)
            
            # Generate the profile report
            profile = ProfileReport(
                df, 
                title=f"Reporte de Perfil de Datos: {file_name}",
                explorative=True
            )
            
            # Save the report to an HTML file
            profile.to_file(report_path)
            
            print(f"Reporte guardado exitosamente en: {report_path}\
")
            
        except Exception as e:
            print(f"** Error al generar el reporte para {file_name}: {e} **\
")

if __name__ == '__main__':
    generar_reporte_perfil_datos()
