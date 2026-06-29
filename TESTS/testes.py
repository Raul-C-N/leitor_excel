#área de teste
# from PyExcel import ler_colunas_por_linha_especifica, ler_excel_inteiro
# from funcoes_texto import palavra_no_texto


# pergunta_vidro="""ocorreu a quebra de vidro de veículo no texto abaixo? responda apenas com sim ou não:"""
# texto="""A vítima relata o furto ou perda de sua carteira de documentos, incluindo CNH, documento do veículo moto e R$ 300,00 em dinheiro, ocorrido no centro de SP, na rua Barão de Dubrat, número 325. O delegado de polícia considera o caso como crime, com base na narrativa da vítima via Boletim de Ocorrência Eletrônico, e orienta a vítima a comparecer à delegacia com o BO para fornecer mais informações sobre autoria."""
# texto1= "O declarante encontrou o vidro do passageiro de seu veículo quebrado, estacionado na Av. Conselheiro Carrão, em frente ao Clube Atlético Carrão, e constatou o furto de seu celular e bilhete do idoso. O Boletim Eletrônico de Ocorrência foi elaborado pelo próprio declarante, que foi orientado a comparecer ao Distrito Policial para complementar informações e verificar a necessidade de perícia no veículo."
# texto2="""O veículo de locadora, placa TBW***1, teve o vidro do passageiro quebrado e o estepe roubado, além do acionador do porta-malas danificado. A vítima registrou a ocorrência eletronicamente, e o delegado considera o caso como crime, orientando a vítima a comparecer à delegacia com o boletim para auxiliar na investigação de autoria."""

# perguntar_ia(texto)
# perguntar_ia(texto1)
# perguntar_ia(texto2)

# palavra_no_texto(texto,"vidro")
# palavra_no_texto(texto1,"vidro")
# palavra_no_texto(texto2,"vidro")
# palavra_no_texto(x,"vidro")

# texto1_ext=extrair_trecho(texto1,"vidro",100)
# texto2_ext=extrair_trecho(texto2,"vidro",100)

# perguntar_ia(pergunta_vidro+texto1_ext)
# perguntar_ia(pergunta_vidro+texto2_ext)

# ######temporizador
# inicio = datetime.now()
# print("Início:", inicio)

# print("Executando...")
# # perguntar_ia(pergunta_vidro + texto1_ext)
# perguntar_ia(pergunta_vidro + texto2_ext)

# fim = datetime.now()
# print("Fim:", fim)

# # cálculo do tempo
# duracao = fim - inicio
# print("Tempo de execução:", duracao)


# ########testes PyExcel.py
# pergunta_vidro="""ocorreu a quebra de vidro de veículo no texto abaixo? responda apenas com sim ou não:"""
# excel="DECAP - fev mar e abril 2026 - art. 155 e 157 - infocrim - analise das ocorrencias e MO -v.2.xlsx"
# abril=ler_excel_inteiro(excel,2)

# # for i in ler_colunas_por_linha_especifica(abril, 1).keys():
#     # print(i)

# # print(ler_colunas_por_linha_especifica(abril, 1)["Historico"])

# inicio_tempo_total=datetime.now()
# n=0
# lista_resultados=[]
# lista_tempo_processamento=[]
# lista_respostas_ia=[]
# for i in range(0, 100):  # Ajuste o range conforme necessário
#     x = ler_colunas_por_linha_especifica(abril, n)["Historico"]
#     y = ler_colunas_por_linha_especifica(abril, n)["NumeroBO"]
#     palavra_no_texto(x,"vidro")
#     if palavra_no_texto(x,"vidro") == False:
#         print("A palavra 'vidro' não foi encontrada no texto.")
#         n+=1
#     else:
#         x_ext=extrair_trecho(x,"vidro",100)
#     ###IA
#         inicio = datetime.now()
#         print("Início:", inicio)

#         print("Executando...")
#         # perguntar_ia(pergunta_vidro + texto1_ext)
#         resposta_ia_temp=perguntar_ia(pergunta_vidro + x_ext)

#         fim = datetime.now()
#         print("Fim:", fim)

#         # cálculo do tempo
#         duracao = fim - inicio
#         print("Tempo de execução:", duracao)
#         print(x_ext)
#         lista_BO.append(y)
#         lista_resultados.append(x_ext)
#         lista_respostas_ia.append(resposta_ia_temp)
#         lista_tempo_processamento.append(duracao)
#         n+=1
# fim_tempo_total=datetime.now()
# duracao_total=fim_tempo_total-inicio_tempo_total
# print("Tempo total de execução:", duracao_total)

# ###soma de tempo da lista de processamento
# from datetime import timedelta

# lista = lista_tempo_processamento

# total = sum(lista, timedelta())

# print("processamento efetivo: " + str(total))  # 0:30:00
# print("Tempo total de execução:", duracao_total)

###TESTE navogacao_arquivos
import os
from pathlib import Path

Path.cwd()
from MODELS import navegacao_arquivos

# passo 1 - pegar caminho do arquivo excel
# caminho_excel_0 = navegacao_arquivos.pegar_caminho_primeiro_excel_pasta_planilhas()
#envia para o processador de dados do excel

navegacao_arquivos.diretorio_atual()
navegacao_arquivos.pegar_caminho_primeiro_excel_pasta_planilhas()

