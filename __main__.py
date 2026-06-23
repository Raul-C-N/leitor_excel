# app/__main__.py
# from __init__ import *

from . import navegacao_arquivos

#coordenacao de execução do programa


def main():
    print("Aplicação executando")
    try:
        arquivos = navegacao_arquivos.listar_excel()
        for arq in arquivos:
            print(arq)

    except Exception as e:
        print(f"Erro ao executar a aplicação: {e}")
        return exit()

    
    print("Aplicação finalizada com sucesso")


# fim do arquivo main
if __name__ == "__main__":
    main()
    