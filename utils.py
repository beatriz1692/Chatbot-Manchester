import re

def extract_number(text):
    """Extrai o primeiro número inteiro de um texto"""
    match = re.search(r'\d+', text)
    return int(match.group()) if match else 0

def get_input(prompt):
    try:
        return input(prompt).strip().lower()
    except KeyboardInterrupt:
        print("\nEncerrando chatbot.")
        exit()
