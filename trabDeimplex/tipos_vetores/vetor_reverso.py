class vetor_reverso:
    def gera_vetore_reverso(inc, fim, stp):
        vetores = []
        for n in range(inc, fim + 1, stp):
            vetor = list(range(n, 0, -1))
            vetores.append(vetor)
            
        return vetores