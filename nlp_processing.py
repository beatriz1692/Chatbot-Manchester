import spacy

# Carrega o modelo de linguagem do spaCy (português)
nlp = spacy.load("pt_core_news_sm")

# Lista de sintomas conhecidos — pode ser expandida!
KNOWN_SYMPTOMS = [
    "dor no peito", "dificuldade para respirar", "febre",
    "dor de cabeça", "náusea", "vômito", "tontura",
    "diarreia", "convulsão", "desmaio", "dor abdominal",
    "sangramento", "palpitações", "fraqueza", "inchaço"
]

def extract_symptom(text):
    """
    Tenta identificar um sintoma conhecido na frase digitada pelo usuário.
    """
    text = text.lower()
    doc = nlp(text)

    for sintoma in KNOWN_SYMPTOMS:
        if sintoma in text:
            return sintoma

    return "sintoma não identificado"
