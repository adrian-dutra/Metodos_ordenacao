class InsertionSort:
    def insertion_sort(vetor):
        for i in range(1, len(vetor)):
            pivo = vetor[i]
            j = i - 1
            while j >= 0 and pivo < vetor[j]:
                vetor[j + 1] = vetor[j]
                j -= 1
            vetor[j + 1] = pivo
            
        return vetor