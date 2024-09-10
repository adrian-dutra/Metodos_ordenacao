import random
import time


def lista_aleatoria(inc, fim, stp, rpt):
    bolha = 0

    for tamanho in range(inc, fim + 1, stp):
        for _ in range(rpt):
            lista_ale = [random.randint(1,1500) for _ in range(tamanho)]

            bolha += ordena_bolha(lista_ale)
        
    
    tempo_medio_bolha = bolha_media(bolha, rpt)





def ordena_bolha(lista_passada):
    lista = lista_passada

    tempo_inicial = time.time()
    for pula_num in range(len(lista) - 1, 0, -1):
        for i in range(pula_num):
            if lista[i] > lista[i + 1]:
                lista[i], lista[i + 1] = lista[i + 1], lista[i]
    tempo_final = time.time()
    tempo_bolha = tempo_final - tempo_inicial

    return tempo_bolha


def ordena_selecao(lista_passada):
    lista = lista_passada
    n = len(lista)

    tempo_inicial = time.time()
    for i in range(n):
        menor = i
        for j in range(i + 1, n):
            if lista[menor] > lista[j]:
                menor = j
        lista[i], lista[menor] = lista[menor], lista[i]
    tempo_final = time.time()
    tempo_selecao = tempo_final - tempo_inicial

    return tempo_selecao


def ordena_insercao(lista_passada):
    lista = lista_passada
    n = len(lista_passada)

    tempo_inicial = time.time()
    for j in range(1, n):
        key = lista[j]
        i = j - 1
        while i >= 0 and lista[i] > key:
            lista[i + 1] = lista[i]
            i = i - 1
            lista[i + 1] = key
    tempo_final = time.time()
    tempo_insercao = tempo_final - tempo_inicial
    
    return tempo_insercao

def bolha_media(tempo, rpt):
    media_bolha = tempo / rpt
    return media_bolha

def selecao_media(tempo, rpt):
    media_selecao = tempo / rpt
    return media_selecao

def insercao_media(tempo, rpt):
    media_insercao = tempo / rpt
    return media_insercao