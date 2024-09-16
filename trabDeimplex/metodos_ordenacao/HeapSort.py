class HeapSort:

    @staticmethod
    def swap(arr:list, i:int, j:int) -> None:
        arr[i], arr[j] = arr[j], arr[i]

    @staticmethod
    def heapify(vetor, tamanho_vetor, i):
        largest = i          
        esquerda = 2 * i + 1     
        direita = 2 * i + 2    

        if esquerda < tamanho_vetor and vetor[esquerda] > vetor[largest]:
            largest = esquerda

        if direita < tamanho_vetor and vetor[direita] > vetor[largest]:
            largest = direita

        if largest != i:
            HeapSort.swap(vetor, i, largest)

            HeapSort.heapify(vetor, tamanho_vetor, largest)

    @staticmethod
    def heap_sort(vetor):

        tamanho_vetor = len(vetor)
        
        if tamanho_vetor <= 1:
            return vetor

        for i in range((tamanho_vetor - 1)//2, -1, -1):
            HeapSort.heapify(vetor, tamanho_vetor, i)

        for i in range(tamanho_vetor - 1, 0, -1):
            HeapSort.swap(vetor,i,0)  
            HeapSort.heapify(vetor, i, 0)

        return vetor