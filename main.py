###bubble sort
def bubbleSort(arr):
    for passnum in range(len(arr)-1,0,-1):
        for i in range(passnum):
            if arr[i]>arr[i+1]:
                temp = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = temp
    return arr

###insertion sort
def insertionSort(arr):
    for i in range(1, len(arr)):
        t = arr[i]
        index = i
        for j in range(i -1, -1, -1):  
            if arr[j] > t:
                arr[j + 1] = arr[j]
                index = j
            else:
                break
        if index != i:
            arr[index] = t
    return arr