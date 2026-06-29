
from MODELS import navegacao_arquivos

def main():
    print("Aplicação executando")
    print("Buscando arquivo Excel...")
    try:
        caminho_excel_0 =navegacao_arquivos.pegar_caminho_primeiro_excel_pasta_planilhas()
    except Exception as e:
        print(f"Erro ao executar a aplicação: {e}")
    
    
    print("Aplicação finalizada com sucesso")


# fim do arquivo main
if __name__ == "__main__":
    main()
    