
import pandas as pd
import matplotlib.pyplot as plt
import os

# Define paths
DATA_PATH = 'data/raw/detalle_ventas.csv'
PLOT_PATH = '2_data_understanding/plots/'
PLOT_FILENAME = '02_distribucion_valor_venta.png'

def plot_distribucion_valor_venta():
    """
    Generates and saves a histogram of the total value per sale.
    """
    print(f"--- Generando histograma de valor por venta de {DATA_PATH} ---")

    # Load data
    try:
        df = pd.read_csv(DATA_PATH)
    except FileNotFoundError:
        print(f"Error: Archivo no encontrado en {DATA_PATH}")
        return

    # --- Data Preparation ---
    # Calculate the total value for each sale
    valor_por_venta = df.groupby('venta_id')['total_linea'].sum()

    # --- Plotting ---
    plt.style.use('seaborn-v0_8-whitegrid')
    fig, ax = plt.subplots(figsize=(12, 7))

    ax.hist(valor_por_venta, bins=50, color='lightcoral', edgecolor='black')

    # Formatting
    ax.set_title('Distribución del Valor Total por Venta', fontsize=16, weight='bold')
    ax.set_xlabel('Valor Total de la Venta (USD)', fontsize=12)
    ax.set_ylabel('Frecuencia (Número de Ventas)', fontsize=12)
    ax.axvline(valor_por_venta.mean(), color='red', linestyle='dashed', linewidth=2, label=f'Media: ${valor_por_venta.mean():.2f}')
    ax.axvline(valor_por_venta.median(), color='green', linestyle='dashed', linewidth=2, label=f'Mediana: ${valor_por_venta.median():.2f}')
    ax.legend()
    plt.tight_layout()

    # --- Save Plot ---
    if not os.path.exists(PLOT_PATH):
        os.makedirs(PLOT_PATH)
    
    save_path = os.path.join(PLOT_PATH, PLOT_FILENAME)
    plt.savefig(save_path)

    print(f"Gráfico guardado exitosamente en: {save_path}")

if __name__ == '__main__':
    plot_distribucion_valor_venta()
