
import pandas as pd
import numpy as np
import os

# Configuration
NUM_CLIENTES = 500
DATA_DIR = 'data/processed/'
FILE_PATH = os.path.join(DATA_DIR, 'rfm_data.csv')

def generar_datos_rfm_placeholder():
    """
    Generates a placeholder RFM dataset for use in Phase 4 (Modeling).
    """
    print("--- Generando archivo de datos RFM de marcador de posición ---")
    
    # Create the directory if it doesn't exist
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)
        
    # Generate plausible random data
    data = {
        'cliente_id': range(1, NUM_CLIENTES + 1),
        'recency': np.random.randint(1, 365, size=NUM_CLIENTES), # Days since last purchase
        'frequency': np.random.randint(1, 50, size=NUM_CLIENTES),  # Total number of purchases
        'monetary': np.random.lognormal(mean=7, sigma=1, size=NUM_CLIENTES).round(2) # Total spend, log-normal for realism
    }
    
    df = pd.DataFrame(data)
    
    # Save to CSV
    df.to_csv(FILE_PATH, index=False)
    
    print(f"Archivo de datos RFM guardado exitosamente en: {FILE_PATH}")
    print("Primeras 5 filas:")
    print(df.head())

if __name__ == '__main__':
    generar_datos_rfm_placeholder()

