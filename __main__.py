from MODELS import navegacao_arquivos

def main():
    print("Aplicação executando")
    try:
        navegacao_arquivos.entrar_pasta_leitor_excel()
        arquivo = navegacao_arquivos.listar_excel_local() #pega o primeiro arquivo encontrado na pasta atual
        print(arquivo)

    except Exception as e:
        print(f"Erro ao executar a aplicação: {e}")
        return exit()

    
    print("Aplicação finalizada com sucesso")


# fim do arquivo main
if __name__ == "__main__":
    main()
    