
import random


class vetor_aleatorio:

    def gera_vetor_aleatorio(inc, fim, stp, rpt):
        for n in range(inc, fim + 1, stp):
            print(f"Gerando vetores de tamanho {n}:")
            
            for i in range(rpt):
                vetor = [random.randint(0, n**2) for _ in range(n)]
                print(f"Vetor {i+1} de tamanho {n}: {vetor}")
            
        return vetor
                
    