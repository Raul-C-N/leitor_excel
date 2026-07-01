
import pandas as pd
import os

def ler_excel_inteiro(caminho_arquivo: str, aba: str = None) -> pd.DataFrame:
    """
    1) Lê o arquivo Excel inteiro e o retorna como um DataFrame do pandas.
    2) Permite selecionar a aba desejada.
    
    Ler aba padrão (primeira): df = ler_excel_inteiro("arquivo.xlsx")
    Ler aba específica: df = ler_excel_inteiro("arquivo.xlsx", aba="Sheet1")
    Ler aba pelo índice:
        df = ler_excel_inteiro("arquivo.xlsx", aba=0)  # Primeira aba
        df = ler_excel_inteiro("arquivo.xlsx", aba=1)  # Segunda aba
    OBSERVACAO IMPORTANTE
        sheet_name=None → lê todas as abas (retorna um dicionário de DataFrames)
        sheet_name="nome" → lê aba específica

    """
    try:
        df = pd.read_excel(caminho_arquivo, sheet_name=aba)
        print(f"Arquivo '{caminho_arquivo}' lido com sucesso. Total de linhas: {len(df)}")
        return df
    except FileNotFoundError:
        print(f"Erro: Arquivo não encontrado no caminho: {caminho_arquivo}")
        return pd.DataFrame()
    except Exception as e:
        print(f"Ocorreu um erro ao ler o arquivo Excel: {e}")
        return pd.DataFrame()

def ler_cabecalhos(df: pd.DataFrame) -> list:
    """
    2) Lê e retorna os nomes (cabecalhos) das colunas do arquivo.
    """
    if df.empty:
        return []
    cabecalhos = df.columns.tolist()
    # print("\n--- Cabeçalhos das Colunas ---")
    # print(cabecalhos)
    return cabecalhos

def iterar_sobre_colunas(df: pd.DataFrame) -> list[list]:
    """
    3) Itera sobre as colunas do arquivo e retorna uma lista de seus conteúdos (cada coluna como uma lista).
    """
    if df.empty:
        return []
    
    # O .values.tolist() converte o DataFrame em uma lista de listas, onde cada sublista é uma coluna.
    conteudo_colunas = df.values.tolist()
    print("\n--- Conteúdo das Colunas (Estrutura de Lista de Listas) ---")
    print(f"Total de colunas encontradas: {len(conteudo_colunas)}")
    return conteudo_colunas

def apensar_informacao_na_linha(df: pd.DataFrame, indice_linha: int, nova_informacao: dict) -> pd.DataFrame:
    """
    4) Apensa novas informações em determinada linha por meio do índice da lista do item 3.
    
    Args:
        df: O DataFrame original.
        indice_linha: O índice da linha a ser modificada (baseado na lista de conteúdo das colunas).
        nova_informacao: Um dicionário com as novas chaves/valores a serem inseridos.

    Returns:
        O DataFrame modificado.
    """
    if df.empty:
        print("Erro: O DataFrame está vazio.")
        return df

    # 1. Obter os cabeçalhos (para saber os nomes das colunas)
    cabecalhos = df.columns.tolist()
    
    # 2. Obter o conteúdo atual da linha alvo
    linha_atual = df.iloc[indice_linha]
    print(f"\n--- Linha Alvo (Índice {indice_linha}) antes da modificação ---")
    print(linha_atual)

    # 3. Preparar as novas informações para serem inseridas
    # Criar um dicionário de valores que correspondem aos cabeçalhos
    novos_valores = {}
    for col in cabecalhos:
        if col in nova_informacao:
            novos_valores[col] = nova_informacao[col]
        else:
            # Se a nova informação não tiver um campo para uma coluna existente, mantém o valor antigo
            novos_valores[col] = linha_atual.get(col)

    # 4. Atualizar a linha no DataFrame
    df.loc[indice_linha] = [novos_valores[col] for col in cabecalhos]
    
    print("\n--- Linha Alvo APENSA (Após modificação) ---")
    print(df.iloc[indice_linha])
    
    return df

def ler_colunas_por_linha(df: pd.DataFrame) -> list[dict]:
    """
    5) Lê o conteúdo das colunas de cada linha do arquivo e retorna uma lista de dicionários, onde cada dicionário representa uma linha com seus respectivos campos e valores.
    """
    if df.empty:
        return []
    
    colunas = df.to_dict(orient='records')
    print("\n--- Colunas por Linha (Lista de Dicionários) ---")
    for i, linha in enumerate(colunas):
        print(f"Linha {i}: {linha}")
    return colunas

def ler_colunas_por_linha_especifica(df: pd.DataFrame, indice_linha: int) -> dict:
    """
    6) Lê o histórico de uma linha específica do arquivo e retorna um dicionário com os campos e valores dessa linha.
    """
    if df.empty:
        return {}
    
    if indice_linha < 0 or indice_linha >= len(df):
        print(f"Erro: Índice da linha {indice_linha} está fora do intervalo.")
        return {}
    
    linha_especifica = df.iloc[indice_linha].to_dict()
    print(f"\n--- Histórico da Linha Específica (Índice {indice_linha}) ---")
    print(linha_especifica)
    return linha_especifica

def ler_abas_excel(caminho_arquivo=None) -> list:
    from MODELS import navegacao_arquivos
    if caminho_arquivo is None:
        caminho_arquivo = navegacao_arquivos.pegar_caminho_primeiro_excel_pasta_planilhas()
    abas = list(pd.ExcelFile(caminho_arquivo).sheet_names)
    return abas

########testes
# for i in ler_colunas_por_linha_especifica(marco, 1).keys():
#     print(i)

# print(ler_colunas_por_linha_especifica(marco, 1)["Historico"])
# x = ler_colunas_por_linha_especifica(marco, 1)["Historico"]

# historicos_marco=ler_colunas_por_linha(marco)
# for i in historicos_marco:
#     print(i["Historico"])
    

