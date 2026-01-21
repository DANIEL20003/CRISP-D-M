
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Define paths
DATA_PATH = 'data/processed/rfm_data_with_clusters.csv'
PLOT_PATH = '5_evaluation/plots/'

def analizar_segmentos():
    """
    Analyzes the customer segments by calculating their mean RFM values
    and generating visualizations to compare them.
    """
    print("--- Iniciando Fase 5: Análisis y Evaluación de Segmentos ---")

    # Load data
    try:
        df = pd.read_csv(DATA_PATH)
    except FileNotFoundError:
        print(f"Error: Archivo no encontrado en {DATA_PATH}")
        return

    # --- Calculate Segment Profiles ---
    # Group by cluster and calculate mean for RFM
    segment_profiles = df.groupby('cluster').agg({
        'recency': 'mean',
        'frequency': 'mean',
        'monetary': 'mean'
    }).round(2)

    print("Perfiles de Segmentos (Valores Medios):")
    print(segment_profiles)

    # --- Create Visualizations ---
    if not os.path.exists(PLOT_PATH):
        os.makedirs(PLOT_PATH)

    plt.style.use('seaborn-v0_8-whitegrid')

    # Bar plots for each RFM component
    plot_map = {
        'recency': '03_recency_por_segmento.png',
        'frequency': '04_frequency_por_segmento.png',
        'monetary': '05_monetary_por_segmento.png'
    }

    for col, filename in plot_map.items():
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.barplot(x=segment_profiles.index, y=segment_profiles[col], ax=ax, palette='viridis')
        ax.set_title(f'{col.capitalize()} Media por Segmento', fontsize=16)
        ax.set_xlabel('Segmento (Cluster)', fontsize=12)
        ax.set_ylabel(f'Valor Medio de {col.capitalize()}', fontsize=12)
        
        plot_filename = os.path.join(PLOT_PATH, filename)
        plt.savefig(plot_filename)
        print(f"Gráfico guardado en: {plot_filename}")
        plt.close()

    # Scatter plot for Recency vs Monetary
    fig, ax = plt.subplots(figsize=(12, 8))
    sns.scatterplot(
        data=df,
        x='recency',
        y='monetary',
        hue='cluster',
        palette='viridis',
        s=100,
        alpha=0.7
    )
    ax.set_title('Segmentos de Clientes: Recencia vs. Gasto Monetario', fontsize=16)
    ax.set_xlabel('Recencia (Días)', fontsize=12)
    ax.set_ylabel('Gasto Monetario (USD)', fontsize=12)
    ax.legend(title='Segmento')
    plt.tight_layout()
    scatter_plot_filename = os.path.join(PLOT_PATH, '06_scatterplot_segmentos.png')
    plt.savefig(scatter_plot_filename)
    print(f"Gráfico de dispersión guardado en: {scatter_plot_filename}")
    plt.close()

    print("\n--- Proceso de evaluación finalizado ---")


if __name__ == '__main__':
    analizar_segmentos()
