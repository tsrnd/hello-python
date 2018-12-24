def swap(list, i, j):
    temp = list[i]
    list[i] =  list[j]
    list[j] = temp
    return

def heapify(list, end , i):   
    l=2 * i + 1  
    r=2 * (i + 1)   
    max=i   
    if l < end and list[i] < list[l]:   
        max = l   
    if r < end and list[max] < list[r]:   
        max = r   
    if max != i:   
        swap(list, i, max)   
        heapify(list,end, max)
def heap_sort(list):
    list_copy = list.copy()    
    end = len(list_copy)   
    start = end // 2 - 1
    for i in range(start, -1, -1):   
        heapify(list_copy, end, i)   
    for i in range(end-1, 0, -1):   
        swap(list_copy, i, 0)   
        heapify(list_copy, i, 0) 
    return list_copy

def quick_sort(list, l, r):
    if l < r:
        p = partition(list, l ,r)
        quick_sort(list, l, p - 1)
        quick_sort(list, p + 1, r)
    return list


def partition(list,l, r):
    pivot = list[(l+r)//2]
    i = l
    j = r
    while True:
        while list[i] < pivot:
            i += 1
        while list[j] > pivot:
            j -= 1
        if i >= j:
            return j
        swap(list, i, j)
        

