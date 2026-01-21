import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import joblib
import os

# Define paths
DATA_PATH = 'data/processed/rfm_data.csv'
MODEL_PATH = 'models/'
OUTPUT_DATA_PATH = 'data/processed/'

# Model Parameters
OPTIMAL_K = 4

def entrenar_modelo_final():
    """
    Trains the final K-Means model with the optimal K, saves the model,
    and saves the data with the assigned cluster labels.
    """
    print(f"--- Entrenando modelo K-Means final con K={OPTIMAL_K} ---")

    # Load data
    try:
        df = pd.read_csv(DATA_PATH)
        rfm_features = df[['recency', 'frequency', 'monetary']]
    except FileNotFoundError:
        print(f"Error: Archivo no encontrado en {DATA_PATH}")
        return

    # --- Data Preparation ---
    scaler = StandardScaler()
    rfm_scaled = scaler.fit_transform(rfm_features)

    # --- Train Final Model ---
    kmeans = KMeans(n_clusters=OPTIMAL_K, random_state=42, n_init=10)
    kmeans.fit(rfm_scaled)
    print("Modelo entrenado exitosamente.")

    # --- Save Model Object ---
    if not os.path.exists(MODEL_PATH):
        os.makedirs(MODEL_PATH)
    
    model_filename = os.path.join(MODEL_PATH, 'kmeans_rfm_model.joblib')
    joblib.dump(kmeans, model_filename)
    print(f"Modelo guardado en: {model_filename}")

    # --- Save Data with Cluster Labels ---
    df['cluster'] = kmeans.labels_
    output_filename = os.path.join(OUTPUT_DATA_PATH, 'rfm_data_with_clusters.csv')
    df.to_csv(output_filename, index=False)
    print(f"Datos con etiquetas de cluster guardados en: {output_filename}")
    
    print("\n--- Proceso finalizado ---")


if __name__ == '__main__':
    entrenar_modelo_final()
