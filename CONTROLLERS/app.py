#perguntar o que o usuário deseja fazer: usar modo de análise com IA ou modo de análise sem IA  
def perguntar_modo_analise():
    while True:
        modo = input("Deseja usar o modo de análise com IA ou sem IA? (Digite 'IA' ou 'sem IA'): ").strip().lower()
        if modo in ['ia', 'sem ia']:
            return modo
        else:
            print("Opção inválida. Por favor, digite 'IA' ou 'sem IA'.")

#módulo sem IA
pass

#módulo com IA
def analisar_com_ia():
    from MODELS import navegacao_arquivos
    from MODELS import conector_ollama
    from MODELS import PyExcel
    aba_escolhida = escolher_aba_excel()
    coluna_escolhida = escolher_coluna_excel(aba_escolhida)

#escolher qual aba do arquivo excel o usuário deseja analisar? -> importar função para listar as abas do arquivo excel
def escolher_aba_excel():
    from MODELS import PyExcel
    abas = PyExcel.ler_abas_excel()
    print(f"Abas disponíveis no arquivo Excel: {', '.join(abas)}")
    while True:
        aba_escolhida = input("Digite o nome da aba que deseja analisar: ").strip()
        if aba_escolhida in abas:
            print(f"Aba selecionada para análise: {aba_escolhida}")
            return aba_escolhida
        else:
            print("Aba inválida. Por favor, digite um nome de aba válido.")
            
#escolher coluna do arquivo excel que o usuário deseja analisar -> importar função para listar as colunas do arquivo excel
# def escolher_coluna_excel():
    # from MODELS import PyExcel
    # colunas = PyExcel.ler_colunas_excel()
    # print(f"Colunas disponíveis no arquivo Excel: {', '.join(colunas)}")
    # while True:
        # coluna_escolhida = input("Digite o nome da coluna que deseja analisar: ").strip()
        # if coluna_escolhida in colunas:
            # print(f"Coluna selecionada para análise: {coluna_escolhida}")
            # return coluna_escolhida
        # else:
            # print("Coluna inválida. Por favor, digite um nome de coluna válido.")

def escolher_coluna_excel(coluna=None):
    from MODELS import PyExcel

    colunas = PyExcel.ler_colunas_excel()
    print(f"Colunas disponíveis no arquivo Excel: {', '.join(colunas)}")

    # Se uma coluna foi passada como parâmetro
    if coluna:
        coluna = coluna.strip()
        if coluna in colunas:
            print(f"Coluna selecionada para análise: {coluna}")
            return coluna
        else:
            print(f"A coluna informada '{coluna}' não existe no Excel.")
            print("Será solicitada uma escolha manual.")

    # Fluxo original (prompt)
    while True:
        coluna_escolhida = input("Digite o nome da coluna que deseja analisar: ").strip()

        if coluna_escolhida in colunas:
            print(f"Coluna selecionada para análise: {coluna_escolhida}")
            return coluna_escolhida
        else:
            print("Coluna inválida. Por favor, digite um nome de coluna válido.")

# pergunta = input("Qual coluna você deseja analisar com IA? (Digite o nome da coluna): ").strip()
# print(f"Coluna selecionada para análise com IA: {pergunta}")

#qual pergunta o usuário deseja fazer para a IA / salvar a perqunta como variável

#deseja usar módulo de aceleração? sim ou não
#não -> pass 

#sim -> qual palavra deve ser buscada no texto? -> usar módulo de 'contém palavra'

#######################################
# número de linhas para análise?