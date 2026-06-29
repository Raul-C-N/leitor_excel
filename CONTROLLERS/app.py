#ler dados de qualquer planilha
#automatizar entrada de dados em planilhas
# #inserir dados de qualquer fonte (Word, banco de dados, etc) em planilhas
# #criar gráficos a partir de dados em planilhas
# import pandas as pd
# #ler dados de uma planilha
# df = pd.read_excel('planilha.xlsx')
# #exibir os dados lidos
# print(df)


# #função para ler cabeçalhos de uma planilha
# def ler_cabecalhos(df):
#     cabecalhos = df.columns.tolist()
#     return cabecalhos

# #função para iterar pelos dados de uma coluna da planilha e retorna em uma lista
# def iterar_coluna(df, nome_coluna):
#     valores = []
#     for valor in df[nome_coluna]:
#         # print(valor)
#         valores.append(valor)
#     return valores

# controllers/app.py

from models import navegação_arquivos # IMPORTANTE: Chama o módulo de modelo
import time 

def executar_aplicacao(caminho):
    print("CONTROLLER: Iniciando processamento...")
    time.sleep(0.1) # Simulação de trabalho

    try:
        # 1. Chamar o Modelo para obter dados
        dados = navegação_arquivos.listar_excel(caminho)
        nome_sistema = navegação_arquivos.obter_nome()

        print(f"CONTROLLER: Dados processados com sucesso! (Sistema: {nome_sistema})")
        return dados, True # Retorna os dados e um status de sucesso

    except FileNotFoundError as e:
        print(f"CONTROLLER: ERRO FATAL no Modelo. {e}")
        return None, False
