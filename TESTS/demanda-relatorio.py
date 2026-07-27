
from datetime import datetime
from MODELS import conector_ollama
from MODELS import PyExcel
from MODELS import navegacao_arquivos
from MODELS import funcoes_texto
from CONTROLLERS import app

pergunta_vidro="""ocorreu a quebra de vidro de veículo no texto abaixo? responda apenas com sim ou não:"""
excel=navegacao_arquivos.pegar_caminho_primeiro_excel_pasta_planilhas()
mes=PyExcel.ler_excel_inteiro(excel,0)

# for i in ler_colunas_por_linha_especifica(abril, 1).keys():
    # print(i)

print(PyExcel.ler_colunas_por_linha_especifica(mes, 1)["Historico"])

inicio_tempo_total=datetime.now()
n=0
lista_resultados=[]
lista_tempo_processamento=[]
lista_respostas_ia=[]
lista_BO=[]
for i in range(0, 1000):  # Ajuste o range conforme necessário
    x = PyExcel.ler_colunas_por_linha_especifica(mes, n)["Historico"]
    y = PyExcel.ler_colunas_por_linha_especifica(mes, n)["NumeroBO"]
    funcoes_texto.palavra_no_texto(x,"vidro")
    if funcoes_texto.palavra_no_texto(x,"vidro") == False:
        print("A palavra 'vidro' não foi encontrada no texto.")
        n+=1
    else:
        x_ext=funcoes_texto.extrair_trecho(x,"vidro",100)
    ###IA
        inicio = datetime.now()
        print("Início:", inicio)

        print("Executando...")
        # perguntar_ia(pergunta_vidro + texto1_ext)
        resposta_ia_temp=conector_ollama.perguntar_ia(pergunta_vidro + x_ext)

        fim = datetime.now()
        print("Fim:", fim)

        # cálculo do tempo
        duracao = fim - inicio
        print("Tempo de execução:", duracao)
        print(x_ext)
        lista_BO.append(y)
        lista_resultados.append(x_ext)
        lista_respostas_ia.append(resposta_ia_temp)
        lista_tempo_processamento.append(duracao)
        n+=1
fim_tempo_total=datetime.now()
duracao_total=fim_tempo_total-inicio_tempo_total
print("Tempo total de execução:", duracao_total)

###soma de tempo da lista de processamento
from datetime import timedelta

lista = lista_tempo_processamento

total = sum(lista, timedelta())

print("processamento efetivo: " + str(total))  # 0:30:00
print("Tempo total de execução:", duracao_total)

lista_BO
lista_respostas_ia
lista_resultados



