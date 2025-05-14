import csv
import os
from manchester_rules import classificar_paciente
from train_model import arquivo_csv


def chatbot():
    print("Bem-vindo ao Chatbot Manchester Clínico!")

    # Dados pessoais
    nome = input("Nome do paciente: ")
    idade = int(input("Idade: "))
    sexo = input("Sexo (M/F): ").upper()

    # Sintomas e sinais clínicos
    sintoma = input("Descreva o sintoma principal do paciente: ")
    duracao = int(input("Há quantos dias os sintomas começaram? (somente número): "))
    dor = int(input("Em uma escala de 0 a 10, qual o nível da dor? "))

    temperatura = float(input("Temperatura corporal (°C): "))
    freq_cardiaca = int(input("Frequência cardíaca (bpm): "))
    saturacao = int(input("Saturação de oxigênio (%): "))

    confusao = input("O paciente apresenta confusão mental ou rebaixamento de consciência? (s/n): ").lower() == 's'
    sangramento = input("Há sangramento ativo? (s/n): ").lower() == 's'
    convulsao = input("Apresentou convulsão recente? (s/n): ").lower() == 's'

    # Classificação
    prioridade = classificar_paciente(
        sintoma, duracao, dor, temperatura, freq_cardiaca,
        saturacao, confusao, sangramento, convulsao
    )

    print(f"\nPaciente: {nome} | Idade: {idade} | Sexo: {sexo}")
    print(f"Classificação Manchester sugerida: {prioridade.upper()}")

    # Salvar em CSV
    arquivo_csv = "registros.csv"
    cabecalho = [
        "nome", "idade", "sexo", "sintoma", "duracao", "dor", "temperatura",
        "frequencia_cardiaca", "saturacao", "confusao", "sangramento",
        "convulsao", "classificacao"
    ]
    novo_registro = [
        nome, idade, sexo, sintoma, duracao, dor, temperatura,
        freq_cardiaca, saturacao, confusao, sangramento, convulsao, prioridade
    ]

    arquivo_existe = os.path.isfile(arquivo_csv)
    with open(arquivo_csv, mode='a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        if not arquivo_existe:
            writer.writerow(cabecalho)
        writer.writerow(novo_registro)

    print("\n✅ Dados salvos em registros.csv")

if __name__ == "__main__":
    chatbot()
