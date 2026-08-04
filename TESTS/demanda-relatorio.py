
from datetime import datetime
from MODELS import conector_ollama
from MODELS import PyExcel
from MODELS import navegacao_arquivos
from MODELS import funcoes_texto
from CONTROLLERS import app
from MODELS import resultados
##quebra-vidro
#palavra="vidro"
#pergunta_vidro="""ocorreu a quebra de vidro de veículo no texto abaixo? responda apenas com sim ou não:"""
##aliança
palavra="aliança"
pergunta_vidro="""ocorreu a subtração de uma aliança ou jóia no texto abaixo? responda apenas com sim ou não:"""
###celular
#palavra="celular"
#pergunta_vidro="""ocorreu a subtração de um telefone celular no texto abaixo? responda apenas com sim ou não:"""
###bicicleta
#palavra="bicicleta"
#pergunta_vidro="""O criminoso usou bicicleta para realizar o crime no texto abaixo? responda apenas com sim ou não:"""
###motocicleta
#palavra="moto"
#pergunta_vidro="""O criminoso usou uma moto para realizar o crime no texto abaixo? responda apenas com sim ou não:"""




excel=navegacao_arquivos.pegar_caminho_primeiro_excel_pasta_planilhas()

mes=PyExcel.ler_excel_inteiro(excel,0)

# for i in ler_colunas_por_linha_especifica(abril, 1).keys():
    # print(i)

# print(PyExcel.ler_colunas_por_linha_especifica(mes, 1)["Historico"])

inicio_tempo_total=datetime.now()
n=0
lista_resultados=[]
lista_tempo_processamento=[]
lista_respostas_ia=[]
lista_BO=[]
# for i in range(0, 36788):  # Ajuste o range conforme necessário
# for i in range(0, 23022):  # Ajuste o range conforme necessário
for i in range(0, 202):  # Ajuste o range conforme necessário
    x = PyExcel.ler_colunas_por_linha_especifica(mes, n)["Historico"]
    y = PyExcel.ler_colunas_por_linha_especifica(mes, n)["NumeroBO"]
    funcoes_texto.palavra_no_texto(x,palavra)
    if funcoes_texto.palavra_no_texto(x,palavra) == False:
        print("A palavra '" + palavra + "' não foi encontrada no texto.")
        n+=1
    else:
        x_ext=funcoes_texto.extrair_trecho(x,palavra,100)
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

resultados.criar_excel(lista_BO, lista_respostas_ia, lista_resultados, nome_arquivo="resultado_"+palavra+"_maio_6Seccional.xlsx")
arquivo_saida = "resultado.txt"
arquivo_saida = "resultado_"+palavra+"_maio_6Seccional.txt"

# Grava o conteúdo no TXT
with open(arquivo_saida, "w", encoding="utf-8") as arquivo:
    arquivo.write(f"processamento efetivo: {total}\n")
    arquivo.write(f"Tempo total de execução: {duracao_total}\n")
print(f"Arquivo '{arquivo_saida}' criado com sucesso.")


####contem texto?
#excel=navegacao_arquivos.pegar_caminho_primeiro_excel_pasta_planilhas()
#mes=PyExcel.ler_excel_inteiro(excel,0)
#lista_resultados=[]
#lista_respostas_ia=[]
#lista_BO=[]
#from MODELS import resultados
# #palavra="vidro"
#palavra="aliança"
# #palavra="bicicleta"
#for i in range(len(mes)-1):
#    x = PyExcel.ler_colunas_por_linha_especifica(mes, i)["Historico"]
#    y = PyExcel.ler_colunas_por_linha_especifica(mes, i)["NumeroBO"]
#    funcoes_texto.palavra_no_texto(x,palavra)
#    if funcoes_texto.palavra_no_texto(x,palavra) == False:
#        print("A palavra '" + palavra + "' não foi encontrada no texto.")
#    else:
#        x_ext=funcoes_texto.extrair_trecho(x,palavra,100)
#        lista_BO.append(y)
#        lista_resultados.append(x_ext)
#resultados.criar_excel_contem_palavra(lista_BO=lista_BO, lista_resultados=lista_resultados, nome_arquivo=f"resultado_palavra_{palavra}.xlsx")
#/contem texto?

