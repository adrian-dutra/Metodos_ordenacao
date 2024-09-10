import random
import time

tempo_sort = 0
tempo_insercao = 0
tempo_bolha = 0
tempo_selecao = 0
tempo_final = 0


# ------------------------------------FUNÇÕES --------------------------------
# Essa função cria uma lista aleátoria de 100 números inteiros.(1, 100)
def cem_numeros():
    lista_cem = []
    for c in range(1, 100):
        lista_cem.append(random.randint(1, 100))
    return lista_cem


# Essa função cria uma lista aleátoria de 1.000 números inteiros. (1, 1.000)
def mil_numeros():
    lista_mil = []
    for m in range(1, 1000):
        lista_mil.append(random.randint(1, 1000))
    return lista_mil


# Essa função cria uma lista aleatória de 10.000 números inteiros.(1, 10.000)
def dezmil_numeros():
    lista_dezmil = []
    for d in range(1, 10000):
        lista_dezmil.append(random.randint(1, 10000))
    return lista_dezmil


# Essa função recebe uma lista de números inteiros aleatórios e os coloca em ordem crescente por método de ordenação por bolha
def ordena_bolha(lista_passada):
    # A função time.time inicia a contagem do tempo de execução do código
    tempo_inicial = time.time()
    lista = lista_passada
    # Esse for diminui o tamanho da lista após os números maiores serem colocados nas últimas posições
    for pula_num in range(len(lista) - 1, 0, -1):
        # Coloca o maior número da lista na última posição
        for i in range(pula_num):
            if lista[i] > lista[i + 1]:
                lista[i], lista[i + 1] = lista[i + 1], lista[i]
    # A função time.time finaliza a contagem do tempo de execução do código
    tempo_final = time.time()
    # Define a variável como global para ser usada fora do escopo da função
    global tempo_bolha
    # Subtrai o tempo final pelo inicial para saber o tempo de execução
    tempo_bolha = tempo_final - tempo_inicial
    # Retorna a lista ordenada
    return lista


# Essa função recebe uma lista de números inteiros aleatórios e os coloca em ordem crescente por método de ordenação por seleção
def ordena_selecao(lista_passada):
    # A função time.time inicia a contagem do tempo de execução do código
    tempo_inicial = time.time()
    lista = lista_passada
    # Lê o tamanho da lista
    n = len(lista)
    # Percorre o tamanho da lista
    for i in range(n):
        # Encontra o menor elemento em lista_passada
        menor = i
        for j in range(i + 1, n):
            if lista[menor] > lista[j]:
                menor = j
        # Coloca o menor elemento na posição correta(a esquerda do i os elementos estarão já ordenados, a direita nenhum elemento é menor que os elementos a esquerda de i)
        lista[i], lista[menor] = lista[menor], lista[i]
    # A função time.time finaliza a contagem do tempo de execução do código
    tempo_final = time.time()
    # Define a variável como global para ser usada fora do escopo da função
    global tempo_selecao
    # Subtrai o tempo final pelo inicial para saber o tempo de execução
    tempo_selecao = tempo_final - tempo_inicial
    # Retorna a lista ordenada
    return lista


# Essa função recebe uma lista de números inteiros aleatórios e os coloca em ordem crescente por método de ordenação por bolha
def ordena_insercao(lista_passada):
    # A função time.time inicia a contagem do tempo de execução do código
    tempo_inicial = time.time()
    lista = lista_passada
    # Lê o tamanho da lista
    n = len(lista_passada)
    # Passa pela lista
    for j in range(1, n):
        key = lista[j]
        i = j - 1
        # Põe o elemento lista[j] na posição correta. Todos os elementos à esquerda do i estarão ordenados e os elementos à direita do elemento no i ainda não foram processados (Podem ser menores, maiores, ou iguais ao elemento lista (i))
        while i >= 0 and lista[i] > key:
            lista[i + 1] = lista[i]
            i = i - 1
            lista[i + 1] = key
    # A função time.time finaliza a contagem do tempo de execução do código
    tempo_final = time.time()
    # Define a variável como global para ser usada fora do escopo da função
    global tempo_insercao
    # Subtrai o tempo final pelo inicial para saber o tempo de execução
    tempo_insercao = tempo_final - tempo_inicial
    # Retorna a lista ordenada
    return lista


# Essa função ordena de forma crescente a lista passada, utilizando uma função de ordenação existente em Python
def ordena_sort(lista_passada):
    # A função time.time inicia a contagem do tempo de execução do código
    tempo_inicial = time.time()
    lista = lista_passada
    lista.sort()
    # A função time.time finaliza a contagem do tempo de execução do código
    global tempo_final
    tempo_final = time.time()
    # Define a variável como global para ser usada fora do escopo da função
    global tempo_sort
    # Subtrai o tempo final pelo inicial para saber o tempo de execução
    tempo_sort = tempo_final - tempo_inicial
    # Retorna a lista ordenada
    return lista

# Mostra a média de tempo do método bolha
def bolha_media():
    soma_bolha = 0
    for i in range(1, 101):
        ordena_bolha(mil_numeros())
        soma_bolha += tempo_bolha
        media_bolha = soma_bolha / 100
        return media_bolha

# Mostra a média de tempo do método seleção
def selecao_media():
    soma_selecao = 0
    for i in range(1, 101):
        ordena_selecao(mil_numeros())
        soma_selecao += tempo_selecao
        media_selecao = soma_selecao / 100
        return media_selecao

# Mostra a média de tempo do método inserção
def insercao_media():
    soma_insercao = 0
    for i in range(1, 101):
        ordena_insercao(mil_numeros())
        soma_insercao += tempo_insercao
        media_insercao = soma_insercao / 100
        return media_insercao

# Mostra a média de tempo do método sort
def sort_media():
    soma_sort = 0
    for i in range(1, 101):
        ordena_sort(mil_numeros())
        soma_sort += tempo_sort
        media_sort = soma_sort / 100
        return media_sort


# Essa função faz as chamadas das funções anteriores e a partir da seleção de um menu imprime a lista ordenada de escolha na tela
def menu_imprime():
    print("Escolha uma opção:\n1 - Método de ordenação por bolhas\n"
          "2 - Método de ordenação por seleção\n"
          "3 - Método de ordenação por inserção\n"
          "4 - Pela função do Python sort()\n"
          "5 - Compare os tempos de execução\n"
          "6 - Listas sem ordenação\n"
          "0 - Encerre o programa")
    entrada = int(input("Digite o número: "))
    if entrada == 1:
        print("Escolha uma das listas a ser ordenada:\n1 - Lista de cem números inteiros aleatórios\n"
              "2 - Lista de mil números inteiros aleatórios\n"
              "3 - Lista de dez mil números inteiros aleatórios")
        entrada = int(input("Digite o número: "))

        # MENU Método de ordenação por Bolha -----------------------------------------------------------------------------------------------------
        if entrada == 1:
            print(f"Lista de cem números inteiros aleatórios: {ordena_bolha(lista_cem.copy())}\nO tempo de execução foi: {tempo_bolha} segundos")
                
        elif entrada == 2:
            print(f"Lista de mil números inteiros aleatórios: {ordena_bolha(lista_mil.copy())}\nO tempo de execução foi: {tempo_bolha} segundos")

        elif entrada == 3:
            print(f"Lista de dez mil números inteiros aleatórios: {ordena_bolha(lista_dezmil.copy())}\nO tempo de execução foi: {tempo_bolha} segundos")

    # --------------------------------------------------------------------------------------------------------------------------------------------

    # MENU Método de ordenação por Seleção -------------------------------------------------------------------------------------------------------
    elif entrada == 2:
        print("Escolha uma das listas a ser ordenada:\n1 - Lista de cem números inteiros aleatórios\n"
              "2 - Lista de mil números inteiros aleatórios\n"
              "3 - Lista de mil números inteiros aleatórios")
        entrada = int(input("Digite o número: "))
        if entrada == 1:
            print(
                f"Lista de cem números inteiros aleatórios: {ordena_selecao(lista_cem.copy())}\nO tempo de execução foi: {tempo_selecao} segundos")
        elif entrada == 2:
            print(f"Lista de mil números inteiros aleatórios: {ordena_selecao(lista_mil.copy())}\nO tempo de execução foi: {tempo_selecao} segundos")

        elif entrada == 3:
            print(f"Lista de dez mil números inteiros aleatórios: {ordena_selecao(lista_dezmil.copy())}\nO tempo de execução foi: {tempo_selecao} segundos")

    # ---------------------------------------------------------------------------------------------------------------------------------------------

    # MENU Método de ordenação por Inserção -------------------------------------------------------------------------------------------------------
    elif entrada == 3:
        print("Escolha uma das listas a ser ordenada:\n1 - Lista de cem números inteiros aleatórios\n"
              "2 - Lista de mil números inteiros aleatórios\n"
              "3 - Lista de mil números inteiros aleatórios")
        entrada = int(input("Digite o número: "))
        if entrada == 1:
            print(f"Lista de cem números inteiros aleatórios: {ordena_insercao(lista_cem.copy())}\nO tempo de execução foi: {tempo_insercao} segundos")
        elif entrada == 2:
            print(f"Lista de mil números inteiros aleatórios: {ordena_insercao(lista_mil.copy())}\nO tempo de execução foi: {tempo_insercao} segundos")
        elif entrada == 3:
            print(f"Lista de dez mil números inteiros aleatórios: {ordena_insercao(lista_dezmil.copy())}\nO tempo de execução foi: {tempo_insercao} segundos")
    # ----------------------------------------------------------------------------------------------------------------------------------------------

    # MENU Método de ordenação pela função do Python Sort ------------------------------------------------------------------------------------------
    elif entrada == 4:
        print("Escolha uma das listas a ser ordenada:\n1 - Lista de cem números inteiros aleatórios\n"
                "2 - Lista de mil números inteiros aleatórios\n"
                "3 - Lista de mil números inteiros aleatórios")
        entrada = int(input("Digite o número: "))
        if entrada == 1:
            print(f"Lista de cem números inteiros aleatórios: {ordena_sort(lista_cem.copy())}\ntempo de execução foi: {tempo_sort} microsegundos")
        elif entrada == 2:
            print(f"Lista de mil números inteiros aleatórios: {ordena_sort(lista_mil).copy()}\ntempo de execução foi: {tempo_sort} microsegundos")
        elif entrada == 3:
            print(f"Lista de dez mil números inteiros aleatórios: {ordena_sort(lista_dezmil.copy())}\ntempo de execução foi: {tempo_sort} microsegundos")
    # ------------------------------------------------------------------------------------------------------------------------------------------------
    # MENU Mostra os tempos de execução de cada método de ordenação
    elif entrada == 5:
        print(f"A média do tempo de execução do Método Bolha foi: {bolha_media()} segundos")

        print(f"A média do tempo de execução do Método Seleção foi: {selecao_media()} segundos")

        print(f"A média do tempo de execução do Método Insercao foi: {insercao_media()} segundos")

        print(f"A média do tempo de execução do Método Sort foi: {sort_media()} microsegundos")
    # MENU Mostra as listas sem ordenação
    elif entrada == 6:
        print("Escolha uma opção:\n"
                "1 - Lista de Cem números\n"
                "2 - Lista de Mil números\n"
                "3 - Lista de Dez Mil números")
        opcao = int(input("Digite o número: "))
        if opcao == 1:
            print(lista_cem)
        elif opcao == 2:
            print(lista_mil)
        elif opcao == 3:
            print(lista_dezmil)

    elif entrada == 0:
        print("\nPrograma encerrado!")
    else:
        print("\nOpção inválida!")


# ------------------------------------------------------------------FIM----------------------------------------------------------------------------

# Listas salvas
lista_cem = cem_numeros()
lista_mil = mil_numeros()
lista_dezmil = dezmil_numeros()
# Chamada de funções
menu_imprime()
