import random

class QuickSort:
    # @staticmethod
    # def partition(vetor, low, high):
    #     pivo = vetor[high]
    #     i = low - 1

    #     for j in range(low, high):
    #         if vetor[j] <= pivo:

    #             i = i + 1
    #             vetor[i], vetor[j] = vetor[j], vetor[i]

    #     vetor[i + 1], vetor[high] = vetor[high], vetor[i + 1]
    #     return i + 1

    # @staticmethod
    # def quick_sort(vetor, low, high):
    #     if low < high:
    #         pi = QuickSort.partition(vetor, low, high)
            
    #         QuickSort.quick_sort(vetor, low, pi - 1)
    #         QuickSort.quick_sort(vetor, pi + 1, high)
    @staticmethod
    def median_of_three(vetor, low, high):
        mid = (low + high) // 2
        if vetor[low] > vetor[mid]:
            vetor[low], vetor[mid] = vetor[mid], vetor[low]
        if vetor[low] > vetor[high]:
            vetor[low], vetor[high] = vetor[high], vetor[low]
        if vetor[mid] > vetor[high]:
            vetor[mid], vetor[high] = vetor[high], vetor[mid]
        return mid

    @staticmethod
    def partition(vetor, low, high):
        mid = QuickSort.median_of_three(vetor, low, high)
        vetor[mid], vetor[high] = vetor[high], vetor[mid]  # Usa o mediano como pivô
        pivo = vetor[high]
        i = low - 1

        for j in range(low, high):
            if vetor[j] <= pivo:
                i = i + 1
                vetor[i], vetor[j] = vetor[j], vetor[i]

        vetor[i + 1], vetor[high] = vetor[high], vetor[i + 1]
        return i + 1

    @staticmethod
    def quick_sort(vetor, low, high):
        if low < high:
            pi = QuickSort.partition(vetor, low, high)
            QuickSort.quick_sort(vetor, low, pi - 1)
            QuickSort.quick_sort(vetor, pi + 1, high)
            
    # def gera_vetor_aleatorio(inc, fim, stp):
    #     vetores = []
    #     for n in range(inc, fim + 1, stp):
    #         vetor = [random.randint(0, n**2) for _ in range(n)]
    #         vetores.append(vetor)
            
    #     return vetores
    
    # bah = gera_vetor_aleatorio(100, 1000, 100)
    # arr = []
    # for vet in bah:
    #     arr.append(quick_sort(vet,0,len(vet) - 1 ))
    
    # for i in arr:
    #     print(arr)