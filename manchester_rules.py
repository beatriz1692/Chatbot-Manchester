# rules_engine.py
def classificar_paciente(sintoma, duracao, dor, temperatura, freq_cardiaca,
                          saturacao, confusao, sangramento, convulsao):
    # Condições críticas
    if saturacao < 90 or confusao or sangramento or convulsao:
        return "vermelho"

    # Condições urgentes
    if dor >= 8 and freq_cardiaca > 120:
        return "laranja"

    if temperatura > 39 or dor >= 6:
        return "amarelo"

    # Pouco urgente
    if duracao < 3:
        return "verde"

    # Não urgente
    return "azul"
