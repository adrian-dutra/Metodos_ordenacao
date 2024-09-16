class CountingSort:

    @staticmethod
    def counting_sort(vetor):
        tamanho_vetor = len(vetor)
        entrada = [0] * tamanho_vetor

        count = [0] * (max(vetor) + 1)

        for i in range(0, tamanho_vetor):
            count[vetor[i]] += 1

        for i in range(1, (max(vetor) + 1)):
            count[i] += count[i - 1]

        i = tamanho_vetor - 1
        while i >= 0:
            entrada[count[vetor[i]] - 1] = vetor[i]
            count[vetor[i]] -= 1
            i -= 1

        for i in range(0, tamanho_vetor):
            vetor[i] = entrada[i]
        
        return vetor