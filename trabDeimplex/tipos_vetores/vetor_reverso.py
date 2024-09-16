class vetor_reverso:
    def gera_vetore_reverso(inc, fim, stp):
        vetores = []
        for tamanho in range(inc, fim + 1, stp):
            vetor = list(range(tamanho, 0, -1))
            vetores.append(vetor)
            
        return vetores