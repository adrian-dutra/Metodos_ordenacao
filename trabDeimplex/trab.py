import random
import timeit
from metodos_ordenacao.BubbleSort import *
from metodos_ordenacao.InsertionSort import *
from metodos_ordenacao.QuickSort import *
from metodos_ordenacao.CoutingSort import *
from metodos_ordenacao.HeapSort import *
from metodos_ordenacao.MergeSort import *
from tipos_vetores.vetor_aleatorio import *
from tipos_vetores.vetor_ordenado import *
from tipos_vetores.vetor_reverso import *
from tipos_vetores.vetor_quase_ordenado import *

class trab:
    #Cria variaveis para armazenar valores
    tamanhos_vetores = []
    tempos_insertion_aleatorio = []
    tempos_bubble_aleatorio = []
    tempos_merge_aleatorio = []
    tempos_heap_aleatorio = []
    tempos_quick_aleatorio = []
    tempos_countin_aleatorio = []
    
    tempos_insertion_reverso = []
    tempos_bubble_reverso = []
    tempos_merge_reverso = []
    tempos_heap_reverso = []
    tempos_quick_reverso = []
    tempos_countin_reverso = []
    
    tempos_insertion_ordenado = []
    tempos_bubble_ordenado = []
    tempos_merge_ordenado = []
    tempos_heap_ordenado = []
    tempos_quick_ordenado = []
    tempos_countin_ordenado = []
    
    tempos_insertion_quase_ordenado = []
    tempos_bubble_quase_ordenado = []
    tempos_merge_quase_ordenado = []
    tempos_heap_quase_ordenado = []
    tempos_quick_quase_ordenado = []
    tempos_countin_quase_ordenado = []
    
    rpt = int(input())
    inc = 100
    fim = 1000
    stp = 100
    
    while rpt != 0:
        vet_aleatorio = vetor_aleatorio.gera_vetor_aleatorio()
        vet_reverso = vetor_reverso.gera_vetore_reverso(inc, fim, stp)
        vet_ordenado = vetor_ordenado.gera_vetor_ordenado(inc, fim, stp)
        vet_quase_ordenado = vetor_quase_ordenado.gera_vetor_quase_ordenado(inc, fim, stp)
    
        # ======================ALEATORIO====================
        
    
    
    
    
    
    
    
    #Mostra os resultados no terminal
    print("[[aleatorio]]")
    print("n   insertions   selections   mergesorts   heapsorts   quicksorts   countingsorts")
    print("-------------------------------------------------------------------------------")
    for i in range(rpt):
        print("{:.0f}    {:.6f}    {:.6f}    {:.6f}    {:.6f}    {:.6f}    {:.6f}".format(
            tamanhos_vetores[i], 
            tempos_insertion_aleatorio = [i],
            tempos_bubble_aleatorio = [i],
            tempos_merge_aleatorio = [i],
            tempos_heap_aleatorio = [i],
            tempos_quick_aleatorio = [i],
            tempos_countin_aleatorio = [i]
        ))
    print()
    
    print("[[reverso]]")
    print("n   insertions   selections   mergesorts   heapsorts   quicksorts   countingsorts")
    print("-------------------------------------------------------------------------------")
    for i in range(rpt):
        print("{:.0f}    {:.6f}    {:.6f}    {:.6f}    {:.6f}    {:.6f}    {:.6f}".format(
            tamanhos_vetores[i], 
            tempos_insertion_reverso = [i],
            tempos_bubble_reverso = [i],
            tempos_merge_reverso = [i],
            tempos_heap_reverso = [i],
            tempos_quick_reverso = [i],
            tempos_countin_reverso = [i]
        ))
    print()
    
    print("[[ordenado]]")
    print("n   insertions   selections   mergesorts   heapsorts   quicksorts   countingsorts")
    print("-------------------------------------------------------------------------------")
    for i in range(rpt):
        print("{:.0f}    {:.6f}    {:.6f}    {:.6f}    {:.6f}    {:.6f}    {:.6f}".format(
            tamanhos_vetores[i], 
            tempos_insertion_ordenado = [i],
            tempos_bubble_ordenado = [i],
            tempos_merge_ordenado = [i],
            tempos_heap_ordenado = [i],
            tempos_quick_ordenado = [i],
            tempos_countin_ordenado = [i]
        ))
    print()
    
    print("[[Quase ordenado]]")
    print("n   insertions   selections   mergesorts   heapsorts   quicksorts   countingsorts")
    print("-------------------------------------------------------------------------------")
    for i in range(rpt):
        print("{:.0f}    {:.6f}    {:.6f}    {:.6f}    {:.6f}    {:.6f}    {:.6f}".format(
            tamanhos_vetores[i], 
            tempos_insertion_quase_ordenado = [i],
            tempos_bubble_quase_ordenado = [i],
            tempos_merge_quase_ordenado = [i],
            tempos_heap_quase_ordenado = [i],
            tempos_quick_quase_ordenado = [i],
            tempos_countin_quase_ordenado = [i]
        ))   
