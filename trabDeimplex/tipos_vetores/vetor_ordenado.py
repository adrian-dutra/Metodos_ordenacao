
class vetor_ordenado:
    
    def gera_vetor_ordenado(inc, fim, stp):
        vetores = [] 
        for n in range(inc, fim + 1, stp):
            vetor = list(range(1, n + 1))
            vetores.append(vetor)
            
        return vetores