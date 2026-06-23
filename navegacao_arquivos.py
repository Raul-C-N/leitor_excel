# import glob

# def listar_excel():
#     arquivos = glob.glob("*.xlsx")
#     print(f"Arquivo Excel encontrado: {arquivos}")
    
#     if not arquivos:
#         print("Nenhum arquivo Excel encontrado.")
    
#     return arquivos

# import glob


from pathlib import Path

def listar_excel():
    # arquivos = list(Path(".").glob("*.xlsx"))
    arquivos = list(Path(".").glob("*.xlsx"))
    pasta = Path("planilhas_excel")
    arquivos_absolutos = [str(arq.resolve()) for arq in pasta.glob("*.xlsx")]

    print(f"Arquivos Excel encontrados: {arquivos_absolutos}")
    
    if not arquivos_absolutos:
        print("Nenhum arquivo Excel encontrado.")
    
    return arquivos_absolutos

