import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import joblib

# Carregar os dados
arquivo_csv = "registros.csv"
df = pd.read_csv(arquivo_csv)

# Visualizar os dados carregados (opcional)
print("Dados carregados:")
print(df.head())

# Pré-processamento
# Convertendo variáveis categóricas para numéricas
label_encoder = LabelEncoder()

# 'Sexo' é uma variável categórica que precisamos codificar
df['sexo'] = label_encoder.fit_transform(df['sexo'])

# 'Sim/Não' para 'confusão', 'sangramento' e 'convulsão' (1 = sim, 0 = não)
df['confusao'] = df['confusao'].apply(lambda x: 1 if x else 0)
df['sangramento'] = df['sangramento'].apply(lambda x: 1 if x else 0)
df['convulsao'] = df['convulsao'].apply(lambda x: 1 if x else 0)

# Selecionando features (entradas) e target (saída)
X = df[['idade', 'sexo', 'duracao', 'dor', 'temperatura', 'frequencia_cardiaca', 'saturacao', 'confusao', 'sangramento', 'convulsao']]
y = df['classificacao']

# Dividir os dados em conjunto de treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Treinar o modelo (Random Forest)
modelo = RandomForestClassifier(n_estimators=100, random_state=42)
modelo.fit(X_train, y_train)

# Avaliar o modelo
acuracia = modelo.score(X_test, y_test)
print(f"Acurácia do modelo: {acuracia * 100:.2f}%")

# Salvar o modelo treinado
joblib.dump(modelo, "modelo_manchester.pkl")
print("Modelo treinado e salvo como 'modelo_manchester.pkl'")

