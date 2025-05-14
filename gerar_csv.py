import pandas as pd

# Dados de exemplo
data = {
    "nome": ["João", "Maria", "Pedro", "Ana"],
    "idade": [45, 30, 50, 40],
    "sexo": ["M", "F", "M", "F"],
    "sintoma": ["Dor de cabeça", "Enjoo", "Choro", "Dor abdominal"],
    "duracao": [2, 3, 5, 3],
    "dor": [10, 7, 6, 8],
    "temperatura": [38.5, 37.5, 36.5, 37.8],
    "frequencia_cardiaca": [95, 80, 75, 90],
    "saturacao": [98, 100, 99, 97],
    "confusao": [1, 0, 0, 1],
    "sangramento": [0, 1, 0, 0],
    "convulsao": [0, 0, 0, 1],
    "classificacao": ["vermelho", "amarelo", "verde", "laranja"]
}

# Criar DataFrame
df = pd.DataFrame(data)

# Salvar em CSV
df.to_csv("registros.csv", index=False)

print("CSV gerado com sucesso!")
