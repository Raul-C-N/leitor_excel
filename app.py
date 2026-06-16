#ler dados de qualquer planilha
#automatizar entrada de dados em planilhas
#inserir dados de qualquer fonte (Word, banco de dados, etc) em planilhas
#criar gráficos a partir de dados em planilhas
import pandas as pd
#ler dados de uma planilha
df = pd.read_excel('planilha.xlsx')
#exibir os dados lidos
print(df)


#função para ler cabeçalhos de uma planilha
def ler_cabecalhos(df):
    cabecalhos = df.columns.tolist()
    return cabecalhos

#função para iterar pelos dados de uma coluna da planilha e retorna em uma lista
def iterar_coluna(df, nome_coluna):
    valores = []
    for valor in df[nome_coluna]:
        # print(valor)
        valores.append(valor)
    return valores
