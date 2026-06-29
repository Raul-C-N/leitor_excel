#teste de presença da palavra
def palavra_no_texto(texto, palavra):
    return palavra.lower() in texto.lower()


def extrair_trecho(texto, palavra, x):
    # Encontrar a posição da palavra
    pos = texto.lower().find(palavra.lower())
    
    if pos == -1:
        return ""  # palavra não encontrada
    
    # Definir início e fim do corte
    inicio = max(0, pos - x)
    fim = pos + len(palavra) + x
    
    return texto[inicio:fim]

