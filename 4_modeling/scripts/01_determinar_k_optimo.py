
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import os

# Define paths
DATA_PATH = 'data/processed/rfm_data.csv'
PLOT_PATH = '5_evaluation/plots/'

def determinar_k_optimo():
    """
    Calculates and plots the Elbow Method and Silhouette Scores for a range of k values.
    """
    print("--- Determinando el número óptimo de clusters (K) ---")

    # Load data
    try:
        df = pd.read_csv(DATA_PATH)
        rfm_features = df[['recency', 'frequency', 'monetary']]
    except FileNotFoundError:
        print(f"Error: Archivo no encontrado en {DATA_PATH}")
        return

    # --- Data Preparation ---
    # Standardize the features
    scaler = StandardScaler()
    rfm_scaled = scaler.fit_transform(rfm_features)

    # --- Calculate Scores for a Range of K ---
    k_range = range(2, 11)
    inertia_scores = []
    silhouette_scores = []

    for k in k_range:
        kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
        kmeans.fit(rfm_scaled)
        inertia_scores.append(kmeans.inertia_)
        silhouette_scores.append(silhouette_score(rfm_scaled, kmeans.labels_))
    
    print("Cálculos de inercia y silueta completados.")

    # Create plot directory if it doesn't exist
    if not os.path.exists(PLOT_PATH):
        os.makedirs(PLOT_PATH)

    # --- Plot 1: Elbow Method ---
    plt.style.use('seaborn-v0_8-whitegrid')
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(k_range, inertia_scores, 'bo-')
    ax.set_title('Método del Codo (Elbow Method)', fontsize=16)
    ax.set_xlabel('Número de Clusters (K)', fontsize=12)
    ax.set_ylabel('Inercia', fontsize=12)
    elbow_plot_path = os.path.join(PLOT_PATH, '01_elbow_method.png')
    plt.savefig(elbow_plot_path)
    print(f"Gráfico del Método del Codo guardado en: {elbow_plot_path}")
    plt.close()

    # --- Plot 2: Silhouette Scores ---
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(k_range, silhouette_scores, 'ro-')
    ax.set_title('Puntuaciones de Silueta (Silhouette Scores)', fontsize=16)
    ax.set_xlabel('Número de Clusters (K)', fontsize=12)
    ax.set_ylabel('Coeficiente de Silueta', fontsize=12)
    silhouette_plot_path = os.path.join(PLOT_PATH, '02_silhouette_scores.png')
    plt.savefig(silhouette_plot_path)
    print(f"Gráfico de Puntuaciones de Silueta guardado en: {silhouette_plot_path}")
    plt.close()
    
    print("\n--- Proceso finalizado ---")

if __name__ == '__main__':
    determinar_k_optimo()
