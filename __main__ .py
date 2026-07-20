
from MODELS import navegacao_arquivos
from CONTROLLERS import app

def main():
    print("Aplicação executando")
    print("Buscando arquivo Excel...")
    try:
        caminho_excel_0 =navegacao_arquivos.pegar_caminho_primeiro_excel_pasta_planilhas()
        print(f"Caminho do primeiro arquivo Excel encontrado: {caminho_excel_0}")
    except Exception as e:
        print(f"Erro ao executar a aplicação: {e}")
    #perguntar modo de análise
    app.perguntar_modo_analise()
    #executar função de análise com ou sem IA
    
    
    print("Aplicação finalizada com sucesso")


# fim do arquivo main
if __name__ == "__main__":
    main()
    
#usar este
#criar pasta planilhas_excel na raiz do projeto e colocar arquivos excel para teste