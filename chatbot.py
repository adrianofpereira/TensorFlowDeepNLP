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
        
#Criação de uma lista com todas as conversas
conversas_id = []
for conversa in conversas[:-1]:
    #print(conversa)
    _conversa = conversa.split(' +++$+++ ')[-1][1:-1].replace("'","").replace(" ","")
    #print(_conversa)
    conversas_id.append(_conversa.split(','))

#Separação das Perguntas e Respostas
perguntas = []
respostas = []
for conversa in conversas_id:
    for i in range(len(conversa)-1):
        #print(i)
        print(conversa)
        perguntas.append(id_para_linha[conversa[i]])
        respostas.append(id_para_linha[conversa[i + 1]])
        
def limpa_texto(texto):
    texto = texto.lower()
    texto = re.sub(r"i'm", "i am", texto)
    texto = re.sub(r"he's", "he is", texto)
    texto = re.sub(r"she's", "she is", texto)
    texto = re.sub(r"that's", "that is", texto)
    texto = re.sub(r"what's", "what is", texto)
    texto = re.sub(r"where's", "where is", texto)
    texto = re.sub(r"\'ll", " will", texto)
    texto = re.sub(r"\'ve", " have", texto)
    texto = re.sub(r"\'re", " are", texto)
    texto = re.sub(r"\'d", " would", texto)
    texto = re.sub(r"won't", "will not", texto)
    texto = re.sub(r"can't", "cannot", texto)
    texto = re.sub(r"[-()#/@;:<>{}~+=?.|,]", "", texto)
    return texto

limpa_texto("ExeMplo i'm #@")

#Limpeza das Pergurtas
perguntas_limpas =[]    
for pergunta in perguntas:
    perguntas_limpas.append(limpa_texto(pergunta))
    
#Limpeza Respostas
respostas_limpas =[]    
for resposta in respostas:
    respostas_limpas.append(limpa_texto(resposta))
    
#Criação de um dicionário que mapeia cada palavra e o número de ocorrências
palavras_contagem = {}
for pegunta in perguntas_limpas:
    #print(pergunta)
    for palavra in pergunta.split():
        if palavra not in palavras_contagem:
            palavras_contagem[palavra] = 1
        else:
            palavras_contagem[palavra] += 1

for resposta in respostas_limpas:
    for palavra in resposta.split():
        if palavra not in palavras_contagem:
            palavras_contagem[palavra] = 1
        else:
            palavras_contagem[palavra] += 1
            
#Remoção de palavras não frequentes e tokenização(dois dicionários)
limite = 20 #palavras que aparecem mais de 20x
perguntas_palavras_int = {}
numero_palavra = 0
for palavra, contagem in palavras_contagem.items():
    #print(palavra)
    #print(contagem)
    if contagem >= limite:
        perguntas_palavras_int[palavra] = numero_palavra
        numero_palavra += 1

respostas_palavras_int = {}
numero_palavra = 0
for palavra, contagem in palavras_contagem.items():
    if contagem >= limite:
        respostas_palavras_int[palavra] = numero_palavra
        numero_palavra += 1

#Adição de tokens no dicionário
tokens = ['<PAD>', '<EOS>', '<OUT>', '<SOS>']
for token in tokens:
    perguntas_palavras_int[token] = len(perguntas_palavras_int) + 1

for token in tokens:
    respostas_palavras_int[token] = len(respostas_palavras_int) + 1