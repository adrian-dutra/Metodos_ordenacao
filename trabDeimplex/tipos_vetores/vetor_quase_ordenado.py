import random
class vetor_quase_ordenado:
    def gera_vetor_quase_ordenado(inc, fim, stp):
        vetores = []
        for tamanho in range(inc, fim + 1, stp):
       
            vetor = list(range(1, tamanho + 1))
        
            num_shuffle = max(1, tamanho // 10)
            
            indices = random.sample(range(tamanho), num_shuffle)
            elementos_embaralhados = [vetor[i] for i in indices]
            random.shuffle(elementos_embaralhados)
            
            for idx, valor in zip(indices, elementos_embaralhados):
                vetor[idx] = valor
            
            vetores.append(vetor)
            
        return vetores