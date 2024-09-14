class MergeSort:

    @staticmethod
    def merge(vetor, l, m, r):
        n1 = m - l + 1
        n2 = r - m
    
        L = [0] * (n1)
        R = [0] * (n2)
    
        for i in range(0, n1):
            L[i] = vetor[l + i]
    
        for j in range(0, n2):
            R[j] = vetor[m + 1 + j]
    
        # Merge the temp vetorays back into vetor[l..r]
        i = 0   
        j = 0   
        k = l     
    
        while i < n1 and j < n2:
            if L[i] <= R[j]:
                vetor[k] = L[i]
                i += 1
            else:
                vetor[k] = R[j]
                j += 1
            k += 1
    
        # Copy the remaining elements of L[], if there
        # are any
        while i < n1:
            vetor[k] = L[i]
            i += 1
            k += 1
    
        # Copy the remaining elements of R[], if there
        # are any
        while j < n2:
            vetor[k] = R[j]
            j += 1
            k += 1

    @staticmethod
    def mergeSort(vetor, l, r):
        if l < r:
    
            # Same as (l+r)//2, but avoids overflow for
            # large l and h
            m = l+(r-l)//2
    
            # Sort first and second halves
            MergeSort.mergeSort(vetor, l, m)
            MergeSort.mergeSort(vetor, m+1, r)
            MergeSort.merge(vetor, l, m, r)