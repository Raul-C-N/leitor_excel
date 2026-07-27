import pandas as pd
lista_BO=[]
lista_respostas_ia=[]
lista_resultados=[]

def criar_excel(lista_BO=lista_BO, lista_respostas_ia=lista_respostas_ia, lista_resultados=lista_resultados, nome_arquivo="resultado.xlsx"):
    # Verifica se as listas têm o mesmo tamanho
    if not (len(lista_BO) == len(lista_respostas_ia) == len(lista_resultados)):
        raise ValueError("As três listas devem ter o mesmo tamanho.")

    df = pd.DataFrame({
        "lista_BO": lista_BO,
        "lista_respostas_ia": lista_respostas_ia,
        "lista_resultados": lista_resultados
    })

    df.to_excel(nome_arquivo, index=False)

    return nome_arquivo

def criar_excel_contem_palavra(lista_BO=lista_BO, lista_resultados=lista_resultados, nome_arquivo="resultado_palavra.xlsx"):
    # Verifica se as listas têm o mesmo tamanho
    if not (len(lista_BO) == len(lista_resultados)):
        raise ValueError("As três listas devem ter o mesmo tamanho.")

    df = pd.DataFrame({
        "lista_BO": lista_BO,
        "lista_resultados": lista_resultados
    })

    df.to_excel(nome_arquivo, index=False)

    return nome_arquivo