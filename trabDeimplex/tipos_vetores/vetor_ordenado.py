class vetor_ordenado: 
    def gera_vetor_ordenado(inc, fim, stp):
        vetores = [] 
        for tamanho in range(inc, fim + 1, stp):
            vetor = list(range(1, tamanho + 1))
            vetores.append(vetor)
            
        return vetores