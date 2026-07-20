#perguntar o que o usuário deseja fazer: usar modo de análise com IA ou modo de análise sem IA  
def perguntar_modo_analise():
    while True:
        modo = input("Deseja usar o modo de análise com IA ou sem IA? (Digite 'IA' ou 'sem IA'): ").strip().lower()
        if modo in ['ia', 'sem ia']:
            if modo == 'ia':
                print("Modo de análise com IA selecionado.")
                analisar_com_ia()
            if modo == 'sem ia':
                print("Modo de análise sem IA selecionado.")
                # Aqui você pode chamar a função correspondente ao modo sem IA
                pass  # Substitua por sua função de análise sem IA
            break
        else:
            print("Opção inválida. Por favor, digite 'IA' ou 'sem IA'.")

#módulo sem IA
pass

#módulo com IA
def analisar_com_ia():
    #escolher aba e coluna    
    try:
        aba = escolher_aba_excel()
    except Exception as e:
        print(f"Erro ao escolher aba ou coluna: {e}")
    try:
        coluna = escolher_coluna_excel(aba,None)
    except Exception as e:  
        print(f"Erro ao escolher aba ou coluna: {e}")
    try:
        pergunta_ia = perguntar_pergunta_ia()
    except Exception as e:
        print(f"Erro ao perguntar à IA: {e}")
    try:
        palavra_aceleracao = obter_palavra_aceleracao()
    except Exception as e:
        print(f"Erro ao obter palavra para aceleração: {e}")
    try:
        numero_linhas = perguntar_numero_linhas(None,aba)
    except Exception as e:
        print(f"Erro ao perguntar pelo número de linhas: {e}")
    return aba, coluna, pergunta_ia, palavra_aceleracao, numero_linhas

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

def escolher_coluna_excel(aba=None,coluna=None):
    """fornece terminal de escolha de coluna, dada uma aba. Caso não seja fornecida uma aba, a função de escolha de aba será invocada para escolher a aba.
    

    Args:
        aba (_type_, optional): _description_. Defaults to None.
        coluna (_type_, optional): _description_. Defaults to None.

    Returns:
        coluna escolhida: str
    """
    from MODELS import PyExcel
    if not aba:
        aba = escolher_aba_excel()
    colunas = PyExcel.ler_colunas_excel(None,aba)
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

def perguntar_pergunta_ia():
    """
    Pergunta ao usuário qual pergunta deseja fazer para a IA.
    
    :return: string com a pergunta do usuário
    """
    pergunta = input("Qual pergunta você deseja fazer para a IA? ").strip()
    return pergunta

#deseja usar módulo de aceleração? sim ou não
def obter_palavra_aceleracao():
    """
    Solicita a palavra principal para o módulo de aceleração.
    Retorna a palavra digitada ou None caso o usuário pressione ENTER.
    """
    entrada = input(
        "Digite palavra principal da sua pergunta para o módulo de aceleração "
        "ou aperte ENTER para não utilizar o módulo de aceleração: "
    ).strip()
    
    # Retorna a palavra se algo for digitado, ou None se estiver em branco
    return entrada if entrada else None

def perguntar_numero_linhas(caminho_arquivo=None, aba=None):
    """
    Pergunta ao usuário quantas linhas deseja analisar.
    Retorna uma tupla (1, numero_linhas) com o range a ser usado,
    ou None caso o usuário apenas pressione ENTER.
    """
    from MODELS import PyExcel
    from MODELS import navegacao_arquivos

    # 1. Resolve o caminho do arquivo primeiro se for None
    if caminho_arquivo is None:
        caminho_arquivo = navegacao_arquivos.pegar_caminho_primeiro_excel_pasta_planilhas()

    # 2. Busca o valor máximo com o caminho corrigido
    valor_maximo = PyExcel.quantidade_linhas_excel(caminho_arquivo, aba)

    while True:
        entrada = input(f"Quantas linhas deseja analisar? (Digite um número até {valor_maximo} ou pressione ENTER para ignorar): ").strip()

        # Pressionou ENTER sem digitar nada -> Retorna None
        if entrada == "":
            return (1,valor_maximo)  # Retorna o range completo

        try:
            numero_linhas = int(entrada)
            
            if 0 < numero_linhas <= valor_maximo:
                # Retorna o range inicial ao final
                return (1, numero_linhas)
            else:
                print(f"Por favor, digite um número entre 1 e {valor_maximo}.")
                
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")