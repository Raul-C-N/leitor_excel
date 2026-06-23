# app/__main__.py
# from __init__ import *

from .navegacao_arquivos import listar_excel_local, get_pasta_planilhas, listar_excel, subir_nivel_diretorio, diretorio_atual, entrar_pasta_leitor_excel

#coordenacao de execução do programa


def main():
    print("Aplicação executando")
    try:
        navegacao_arquivos.entrar_pasta_leitor_excel()
        # arquivo = navegacao_arquivos.listar_excel_local() #pega o primeiro arquivo encontrado na pasta atual
        # print(arquivo)

    except Exception as e:
        print(f"Erro ao executar a aplicação: {e}")
        return exit()

    
    print("Aplicação finalizada com sucesso")


# fim do arquivo main
if __name__ == "__main__":
    main()
    