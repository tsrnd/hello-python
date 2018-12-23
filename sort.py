def selectionSort(arr):
    for i in range(len(arr)):  
        minIndex = i    
        for j in range(i+1, len(arr)): 
            if arr[minIndex] > arr[j]: 
                minIndex = j 
                arr[i], arr[minIndex] = arr[minIndex], arr[i] 
    return arr

def bubleSort(arr):
    for i in range(len(arr)):
        for j in range(0, len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j] 
    return arr