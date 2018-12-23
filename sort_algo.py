def insertSort(my_list):
    list = my_list.copy()
    i = 1
    while i < len(list):
        x = list[i]
        j = i - 1
        while j >= 0 and list[j] > x:
            list[j+1] = list[j]
            j = j - 1
        list[j+1] = x
        i = i + 1
    return list

def mergeSort(alist):
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]
        mergeSort(lefthalf)
        mergeSort(righthalf)
        i=j=k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1
            
def quickSort(alist):
    lesser = []
    pivots = []
    greater = []
    if not alist:
        return []
    pivots = [x for x in alist if x == alist[0]]
    lesser = quickSort([x for x in alist if x < alist[0]])
    greater = quickSort([x for x in alist if x > alist[0]])
    return lesser + pivots + greater
