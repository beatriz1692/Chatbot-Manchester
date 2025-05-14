import joblib
import os

# Garante que o caminho funcione em qualquer lugar
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "modelo_manchester.pkl")

# Carrega o modelo treinado
model = joblib.load(MODEL_PATH)

def predict_classification(symptom, duration):
    entrada = f"{symptom} {duration}"
    return model.predict([entrada])[0]
