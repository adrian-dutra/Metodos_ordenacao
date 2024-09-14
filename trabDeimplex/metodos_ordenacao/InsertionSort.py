class InsertionSort:
    def insertion_sort(vetor):
        for i in range(1, len(vetor)):
            key = vetor[i]
            j = i - 1
            while j >= 0 and key < vetor[j]:
                vetor[j + 1] = vetor[j]
                j -= 1
            vetor[j + 1] = key
        return vetor