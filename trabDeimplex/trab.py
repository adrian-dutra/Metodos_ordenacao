import random
import timeit
import time
import numpy as np
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
    
    tempos_medios = {
        "insertion": [],
        "selection": [],
        "merge": [],
        "heap": [],
        "quick": [],
        "counting": []
    }
    
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
    
    for i in range(rpt):
        vetores_aleatorios = vetor_aleatorio.gera_vetor_aleatorio(inc, fim, stp)
        ##################ALEATORIO####################
        for vetor_ale in vetores_aleatorios:
            tamanho_vetor = len(vetor_ale)
            
            vetor_temp = vetor_ale.copy()
            tempo_inicio = time.time()
            BubbleSort.bubble_sort(vetor_temp)
            tempo_fim = time.time()
            tempo_bubble_ale = tempo_fim - tempo_inicio
            tempos_bubble_aleatorio.append(tempo_bubble_ale)
            
            vetor_temp = vetor_ale.copy()
            tempo_inicio = time.time()
            InsertionSort.insertion_sort(vetor_temp)
            tempo_fim = time.time()
            tempo_insertion_ale = tempo_fim - tempo_inicio
            tempos_insertion_aleatorio.append(tempo_insertion_ale)
            
            vetor_temp = vetor_ale.copy()
            tempo_inicio = time.time()
            QuickSort.quick_sort(vetor_temp, 0, len(vetor_temp) - 1)
            tempo_fim = time.time()
            tempo_quick_ale = tempo_fim - tempo_inicio
            tempos_quick_aleatorio.append(tempo_quick_ale)
            
            vetor_temp = vetor_ale.copy()
            tempo_inicio = time.time()
            MergeSort.mergeSort(vetor_temp, 0, len(vetor_temp) - 1)
            tempo_fim = time.time()
            tempo_merge_ale = tempo_fim - tempo_inicio
            tempos_merge_aleatorio.append(tempo_merge_ale)
        
            tempo_inicio = time.time()
            HeapSort.heap_sort(vetor_temp)
            tempo_fim = time.time()
            tempo_heap_ale = tempo_fim - tempo_inicio
            tempos_heap_aleatorio.append(tempo_heap_ale)
            
            vetor_temp = vetor_ale.copy()
            tempo_inicio = time.time()
            CountingSort.counting_sort(vetor_temp)
            tempo_fim = time.time()
            tempo_counting_ale = tempo_fim - tempo_inicio
            tempos_countin_aleatorio.append(tempo_counting_ale)
     
    tempos_medios["insertion"].append(np.mean(tempos_insertion_aleatorio))
    tempos_medios["selection"].append(np.mean(tempos_bubble_aleatorio))
    tempos_medios["merge"].append(np.mean(tempos_merge_aleatorio))
    tempos_medios["heap"].append(np.mean(tempos_heap_aleatorio))
    tempos_medios["quick"].append(np.mean(tempos_quick_aleatorio))
    tempos_medios["counting"].append(np.mean(tempos_countin_aleatorio))
    
    
    
    
    #############REVERSO###############
    vet_reverso = vetor_reverso.gera_vetore_reverso(inc, fim, stp)
    for vetor_rev in vet_reverso:
        tamanhos_vetores.append(len(vetor_rev))
        
        tempo_inicio = time.time()
        BubbleSort.bubble_sort(vetor_rev)
        tempo_fim = time.time()
        tempo_bubble_rev = tempo_fim - tempo_inicio
        tempos_bubble_reverso.append(tempo_bubble_rev)
        
        tempo_inicio = time.time()
        InsertionSort.insertion_sort(vetor_rev)
        tempo_fim = time.time()
        tempo_insertion_rev = tempo_fim - tempo_inicio
        tempos_insertion_reverso.append(tempo_insertion_rev)
        
        tempo_inicio = time.time()
        QuickSort.quick_sort(vetor_rev, 0, len(vetor_rev) - 1)
        tempo_fim = time.time()
        tempo_quick_rev = tempo_fim - tempo_inicio
        tempos_quick_reverso.append(tempo_quick_rev)
        
        tempo_inicio = time.time()
        MergeSort.mergeSort(vetor_rev, 0, len(vetor_rev) - 1)
        tempo_fim = time.time()
        tempo_merge_rev = tempo_fim - tempo_inicio
        tempos_merge_reverso.append(tempo_merge_rev)

        tempo_inicio = time.time()
        HeapSort.heap_sort(vetor_rev)
        tempo_fim = time.time()
        tempo_heap_rev = tempo_fim - tempo_inicio
        tempos_heap_reverso.append(tempo_heap_rev)
        
        tempo_inicio = time.time()
        CountingSort.counting_sort(vetor_rev)
        tempo_fim = time.time()
        tempo_counting_rev = tempo_fim - tempo_inicio
        tempos_countin_reverso.append(tempo_counting_rev)
        
    
    ################ORDENADO####################
    vet_ordenado = vetor_ordenado.gera_vetor_ordenado(inc, fim, stp)
    for vetor_ord in vet_ordenado:
        tempo_inicio = time.time()
        BubbleSort.bubble_sort(vetor_ord)
        tempo_fim = time.time()
        tempo_bubble_ord = tempo_fim - tempo_inicio
        tempos_bubble_ordenado.append(tempo_bubble_ord)
        
        tempo_inicio = time.time()
        InsertionSort.insertion_sort(vetor_ord)
        tempo_fim = time.time()
        tempo_insertion_ord = tempo_fim - tempo_inicio
        tempos_insertion_ordenado.append(tempo_insertion_ord)
        
        tempo_inicio = time.time()
        QuickSort.quick_sort(vetor_ord, 0, len(vetor_ord) - 1)
        tempo_fim = time.time()
        tempo_quick_ord = tempo_fim - tempo_inicio
        tempos_quick_ordenado.append(tempo_quick_ord)
        
        tempo_inicio = time.time()
        MergeSort.mergeSort(vetor_ord, 0, len(vetor_ord) - 1)
        tempo_fim = time.time()
        tempo_merge_ord = tempo_fim - tempo_inicio
        tempos_merge_ordenado.append(tempo_merge_ord)

        tempo_inicio = time.time()
        HeapSort.heap_sort(vetor_ord)
        tempo_fim = time.time()
        tempo_heap_ord = tempo_fim - tempo_inicio
        tempos_heap_ordenado.append(tempo_heap_ord)
        
        tempo_inicio = time.time()
        CountingSort.counting_sort(vetor_ord)
        tempo_fim = time.time()
        tempo_counting_ord = tempo_fim - tempo_inicio
        tempos_countin_ordenado.append(tempo_counting_ord)
    
    
    ###################QUASE ORDENADO###################
    vet_quase_ordenado = vetor_quase_ordenado.gera_vetor_quase_ordenado(inc, fim, stp)
    for vetor_quase in vet_quase_ordenado:
        tempo_inicio = time.time()
        BubbleSort.bubble_sort(vetor_quase)
        tempo_fim = time.time()
        tempo_bubble_quase_ord = tempo_fim - tempo_inicio
        tempos_bubble_quase_ordenado.append(tempo_bubble_quase_ord)
        
        tempo_inicio = time.time()
        InsertionSort.insertion_sort(vetor_quase)
        tempo_fim = time.time()
        tempo_insertion_quase_ord = tempo_fim - tempo_inicio
        tempos_insertion_quase_ordenado.append(tempo_insertion_quase_ord)
        
        tempo_inicio = time.time()
        QuickSort.quick_sort(vetor_quase, 0, len(vetor_quase) - 1)
        tempo_fim = time.time()
        tempo_quick_quase_ord = tempo_fim - tempo_inicio
        tempos_quick_quase_ordenado.append(tempo_quick_quase_ord)
        
        tempo_inicio = time.time()
        MergeSort.mergeSort(vetor_quase, 0, len(vetor_quase) - 1)
        tempo_fim = time.time()
        tempo_merge_quase_ord = tempo_fim - tempo_inicio
        tempos_merge_quase_ordenado.append(tempo_merge_quase_ord)

        tempo_inicio = time.time()
        HeapSort.heap_sort(vetor_quase)
        tempo_fim = time.time()
        tempo_heap_quase_ord = tempo_fim - tempo_inicio
        tempos_heap_quase_ordenado.append(tempo_heap_quase_ord)
        
        tempo_inicio = time.time()
        CountingSort.counting_sort(vetor_quase)
        tempo_fim = time.time()
        tempo_counting_quase_ord = tempo_fim - tempo_inicio
        tempos_countin_quase_ordenado.append(tempo_counting_quase_ord)
    
    
    
    #Mostra os resultados no terminal
    print("[[aleatorio]]")
    print("n   insertions   selections   mergesorts   heapsorts   quicksorts   countingsorts")
    print("-------------------------------------------------------------------------------")
    for i in range(len(vetores_aleatorios)):
        print("{:.0f}    {:.6f}    {:.6f}    {:.6f}    {:.6f}    {:.6f}    {:.6f}".format(
            tamanhos_vetores[i], 
            tempos_insertion_aleatorio[i],
            tempos_bubble_aleatorio[i],
            tempos_merge_aleatorio[i],
            tempos_heap_aleatorio[i],
            tempos_quick_aleatorio[i],
            tempos_countin_aleatorio[i]
        ))
    print()
    
    print("[[reverso]]")
    print("n   insertions   selections   mergesorts   heapsorts   quicksorts   countingsorts")
    print("-------------------------------------------------------------------------------")
    for i in range(len(vet_reverso)):
        print("{:.0f}    {:.6f}    {:.6f}    {:.6f}    {:.6f}    {:.6f}    {:.6f}".format(
            tamanhos_vetores[i], 
            tempos_insertion_reverso[i],
            tempos_bubble_reverso[i],
            tempos_merge_reverso[i],
            tempos_heap_reverso[i],
            tempos_quick_reverso[i],
            tempos_countin_reverso[i]
        ))
    print()
    
    print("[[ordenado]]")
    print("n   insertions   selections   mergesorts   heapsorts   quicksorts   countingsorts")
    print("-------------------------------------------------------------------------------")
    for i in range(len(vet_ordenado)):
        print("{:.0f}    {:.6f}    {:.6f}    {:.6f}    {:.6f}    {:.6f}    {:.6f}".format(
            tamanhos_vetores[i], 
            tempos_insertion_ordenado[i],
            tempos_bubble_ordenado[i],
            tempos_merge_ordenado[i],
            tempos_heap_ordenado[i],
            tempos_quick_ordenado[i],
            tempos_countin_ordenado[i]
        ))
    print()
    
    print("[[Quase ordenado]]")
    print("n   insertions   selections   mergesorts   heapsorts   quicksorts   countingsorts")
    print("-------------------------------------------------------------------------------")
    for i in range(len(vet_quase_ordenado)):
        print("{:.0f}    {:.6f}    {:.6f}    {:.6f}    {:.6f}    {:.6f}    {:.6f}".format(
            tamanhos_vetores[i], 
            tempos_insertion_quase_ordenado[i],
            tempos_bubble_quase_ordenado[i],
            tempos_merge_quase_ordenado[i],
            tempos_heap_quase_ordenado[i],
            tempos_quick_quase_ordenado[i],
            tempos_countin_quase_ordenado[i]
        ))   
