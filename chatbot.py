# Construção do Chatbot com Deep NLP

# importação das bibliotecas
import numpy as np
import tensorflow as tf
import re
import time

linhas = open('movie_lines.txt', encoding='utf-8',
              errors='ignore').read().split('\n')
conversas = open('movie_conversations.txt', encoding='utf-8',
                 errors='ignore').read().split('\n')

# Criação de um dicionário para mapear cada linha do seu ID


id_para_linha = {}


for linha in linhas:
    #print(linha)
    _linha = linha.split(' +++$+++ ')
    #print(_linha)
    if len(_linha) == 5:
        print(_linha[4])
        id_para_linha[_linha[0]] = _linha[4]
        
#Criação de uma lsita com todas as conversas
conversas_id = []
for conversa in conversas[:-1]:
    #print(conversa)
    _conversa = conversa.split(' +++$+++ ')[-1][1:-1].replace("'","").replace(" ","")
    #print(_conversa)
    conversas_id.append(_conversa.split(','))

#Separação dass Perguntas e Respostas
perguntas = []
respostas = []
for conversa in conversas_id:
    for i in range(len(conversa)-1):
        #print(i)
        print(conversa)
        perguntas.append(id_para_linha[conversa[i]])
        respostas.append(id_para_linha[conversa[i + 1]])