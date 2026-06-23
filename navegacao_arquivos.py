import glob

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



