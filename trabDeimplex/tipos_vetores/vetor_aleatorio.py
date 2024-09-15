
import random


class vetor_aleatorio:
    
    def gera_vetor_aleatorio(inc, fim, stp):
        vetores = []
        for n in range(inc, fim + 1, stp):
            vetor = [random.randint(0, n**2) for _ in range(n)]
            vetores.append(vetor)
            
        return vetores
    
    # def bubble_sort(vetor):
    #     n = len(vetor)
    #     for i in range(n):
    #         for j in range(0, n-i-1):
    #             if vetor[j] > vetor[j+1]:
    #                 vetor[j], vetor[j+1] = vetor[j+1], vetor[j]
    #     return vetor
    
    # bah = gera_vetor_aleatorio(100, 1000, 100)
    # arr = []
    # for vet in bah:
    #     arr.append(bubble_sort(vet))
    
    # for i in arr:
    #     print(arr)