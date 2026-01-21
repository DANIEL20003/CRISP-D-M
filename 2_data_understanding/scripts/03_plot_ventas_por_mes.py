
import pandas as pd
import matplotlib.pyplot as plt
import os

# Define paths
DATA_PATH = 'data/raw/ventas.csv'
PLOT_PATH = '2_data_understanding/plots/'
PLOT_FILENAME = '01_ventas_por_mes.png'

def plot_ventas_por_mes():
    """
    Generates and saves a bar chart of the number of sales per month.
    """
    print(f"--- Generando gráfico de ventas por mes de {DATA_PATH} ---")

    # Load data
    try:
        df = pd.read_csv(DATA_PATH)
    except FileNotFoundError:
        print(f"Error: Archivo no encontrado en {DATA_PATH}")
        return

    # --- Data Preparation ---
    # Convert 'fecha' column to datetime
    df['fecha'] = pd.to_datetime(df['fecha'])

    # Extract month and year
    df['mes_ano'] = df['fecha'].dt.to_period('M')

    # Aggregate sales by month
    ventas_mensuales = df['mes_ano'].value_counts().sort_index()

    # --- Plotting ---
    plt.style.use('seaborn-v0_8-whitegrid')
    fig, ax = plt.subplots(figsize=(15, 7))

    ventas_mensuales.plot(kind='bar', ax=ax, color='skyblue', edgecolor='black')

    # Formatting
    ax.set_title('Número de Ventas por Mes', fontsize=16, weight='bold')
    ax.set_xlabel('Mes y Año', fontsize=12)
    ax.set_ylabel('Número de Ventas', fontsize=12)
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()

    # --- Save Plot ---
    if not os.path.exists(PLOT_PATH):
        os.makedirs(PLOT_PATH)
    
    save_path = os.path.join(PLOT_PATH, PLOT_FILENAME)
    plt.savefig(save_path)

    print(f"Gráfico guardado exitosamente en: {save_path}")

if __name__ == '__main__':
    plot_ventas_por_mes()
