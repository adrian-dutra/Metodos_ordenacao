class CountingSort:

    @staticmethod
    def counting_sort(vetor):
        size = len(vetor)
        entrada = [0] * size

        count = [0] * (max(vetor) + 1)

        for i in range(0, size):
            count[vetor[i]] += 1

        for i in range(1, (max(vetor) + 1)):
            count[i] += count[i - 1]

        i = size - 1
        while i >= 0:
            entrada[count[vetor[i]] - 1] = vetor[i]
            count[vetor[i]] -= 1
            i -= 1

        for i in range(0, size):
            vetor[i] = entrada[i]