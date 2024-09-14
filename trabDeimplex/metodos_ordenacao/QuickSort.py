class QuickSort:

    def partition(vetor, low, high):

        pivo = vetor[high]
        i = low - 1

        for j in range(low, high):
            if vetor[j] <= pivo:

                i = i + 1

                (vetor[i], vetor[j]) = (vetor[j], vetor[i])

        (vetor[i + 1], vetor[high]) = (vetor[high], vetor[i + 1])

        return i + 1

    @staticmethod
    def quick_sort(vetor, low, high):
        if low < high:

            pi = QuickSort.partition(vetor, low, high)
            QuickSort.quick_sort(vetor, low, pi - 1)
            QuickSort.quick_sort(vetor, pi + 1, high)