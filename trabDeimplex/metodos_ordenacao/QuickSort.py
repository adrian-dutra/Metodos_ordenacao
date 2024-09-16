class QuickSort:
    @staticmethod
    def meio_vetor(vetor, menor, maior):
        meio = (menor + maior) // 2
        if vetor[menor] > vetor[meio]:
            vetor[menor], vetor[meio] = vetor[meio], vetor[menor]
        if vetor[menor] > vetor[maior]:
            vetor[menor], vetor[maior] = vetor[maior], vetor[menor]
        if vetor[meio] > vetor[maior]:
            vetor[meio], vetor[maior] = vetor[maior], vetor[meio]
        return meio

    @staticmethod
    def partition(vetor, menor, maior):
        meio = QuickSort.meio_vetor(vetor, menor, maior)
        vetor[meio], vetor[maior] = vetor[maior], vetor[meio] 
        pivo = vetor[maior]
        i = menor - 1

        for j in range(menor, maior):
            if vetor[j] <= pivo:
                i = i + 1
                vetor[i], vetor[j] = vetor[j], vetor[i]

        vetor[i + 1], vetor[maior] = vetor[maior], vetor[i + 1]
        return i + 1

    @staticmethod
    def quick_sort(vetor, menor, maior):
        if menor < maior:
            pi = QuickSort.partition(vetor, menor, maior)
            QuickSort.quick_sort(vetor, menor, pi - 1)
            QuickSort.quick_sort(vetor, pi + 1, maior)