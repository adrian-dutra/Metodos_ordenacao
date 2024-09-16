class BubbleSort:
    
    def bubble_sort(vetor):
        tamanho_vetor = len(vetor)
        for i in range(tamanho_vetor):
            for j in range(0, tamanho_vetor-i-1):
                if vetor[j] > vetor[j+1]:
                    vetor[j], vetor[j+1] = vetor[j+1], vetor[j]
        
        return vetor