class vetor_reverso:
    def gera_vetore_reverso(inc, fim, stp):
        for n in range(inc, fim + 1, stp):
            vetor = list(range(n, 0, -1))
            print(f"Vetor de tamanho {n}: {vetor}")
            
        return vetor