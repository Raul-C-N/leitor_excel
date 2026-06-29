import glob
import os
from pathlib import Path

def listar_excel_local():
    arquivos = glob.glob("*.xlsx")
    print(f"Arquivo Excel encontrado: {arquivos}")
    
    if not arquivos:
        print("Nenhum arquivo Excel encontrado.")
    
    return arquivos

def get_pasta_planilhas():
    # return Path.cwd() / "leitor_excel" / "planilhas_excel"
    return Path.cwd() / "planilhas_excel"

def listar_excel(caminho_pasta):
    """
    Lista arquivos .xlsx dentro da pasta informada.
    
    :param caminho_pasta: string ou Path com o caminho da pasta
    :return: lista de caminhos dos arquivos Excel
    """
    pasta = Path(caminho_pasta)

    arquivos = list(pasta.glob("*.xlsx"))
    
    print(f"Arquivos Excel encontrados: {arquivos}")
    
    if not arquivos:
        print("Nenhum arquivo Excel encontrado.")
    
    return arquivos

def subir_nivel_diretorio(caminho):
    """
    Sobe um nível no diretório do caminho informado.
    
    :param caminho: string ou Path com o caminho atual
    :return: Path com o novo caminho (um nível acima)
    """
    return Path(caminho).parent

def diretorio_atual():
    """
    Retorna o diretório atual de trabalho.
    
    :return: Path com o diretório atual
    """
    return Path.cwd()

def mudar_diretorio(caminho):
    """
    Muda o diretório atual de trabalho para o caminho informado.
    
    :param caminho: string ou Path com o novo diretório
    """
    os.chdir(caminho)

def pegar_caminho_primeiro_excel_pasta_planilhas():
    """
    Pega o primeiro arquivo Excel encontrado na pasta de planilhas.
    
    :return: Path do primeiro arquivo Excel ou None se não houver arquivos
    """
    caminho_arquivos_excel=listar_excel(get_pasta_planilhas())
    if not caminho_arquivos_excel:
        print("Nenhum arquivo Excel encontrado na pasta de planilhas.")
        return None
    #escolhe o primeiro arquivo da lista para ter como caminho do arquivo excel
    else:
        return caminho_arquivos_excel[0]




