import random
class vetor_aleatorio:
    
    def gera_vetor_aleatorio(inc, fim, stp):
        vetores = []
        for tamanho in range(inc, fim + 1, stp):
            vetor = [random.randint(0, tamanho**2) for _ in range(tamanho)]
            vetores.append(vetor)
            
        return vetores