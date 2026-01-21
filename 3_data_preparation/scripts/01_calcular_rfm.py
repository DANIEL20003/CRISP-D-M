import pandas as pd
import os

# Define paths
VENTAS_PATH = 'data/raw/ventas.csv'
DETALLE_PATH = 'data/raw/detalle_ventas.csv'
OUTPUT_DIR = 'data/processed/'
OUTPUT_FILE = os.path.join(OUTPUT_DIR, 'rfm_final_data.csv') # Overwrites the placeholder

def calcular_rfm():
    """
    Processes raw sales data to calculate Recency, Frequency, and Monetary
    values for each customer and saves the resulting dataset.
    """
    print("--- Iniciando Fase 3: Cálculo de características RFM ---")

    # Load data
    try:
        ventas_df = pd.read_csv(VENTAS_PATH, parse_dates=['fecha'])
        detalle_df = pd.read_csv(DETALLE_PATH)
    except FileNotFoundError as e:
        print(f"Error: Archivo no encontrado: {e}")
        return

    # --- Data Preparation ---
    # Merge sales and details to get monetary value per transaction line
    df = pd.merge(ventas_df, detalle_df, on='venta_id')

    # --- Calculate RFM ---
    # Determine the snapshot date for recency calculation (day after the last transaction)
    snapshot_date = df['fecha'].max() + pd.Timedelta(days=1)
    print(f"Fecha de referencia (snapshot date) para Recencia: {snapshot_date.date()}")

    # Group by customer
    rfm_df = df.groupby('cliente_id').agg({
        'fecha': lambda date: (snapshot_date - date.max()).days, # Recency
        'venta_id': 'nunique',                                   # Frequency
        'total_linea': 'sum'                                     # Monetary
    })

    # Rename columns for clarity
    rfm_df.rename(columns={'fecha': 'recency', 
                           'venta_id': 'frequency',
                           'total_linea': 'monetary'}, inplace=True)
    
    print("Cálculo de R, F y M completado.")

    # --- Save Final Dataset ---
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    rfm_df.to_csv(OUTPUT_FILE) # Note: index is the cliente_id
    print(f"Dataset RFM final guardado en: {OUTPUT_FILE}")
    
    print("\n--- Proceso de preparación de datos finalizado ---")


if __name__ == '__main__':
    calcular_rfm()
