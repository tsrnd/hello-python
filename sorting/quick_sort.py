def quicksort(mylist, sIndex, eIndex):
    
    # Neu chi co mot phan tu hoac eIndex < sIndex
    if eIndex <= sIndex:
        return
    else:
        pivot = mylist[int((eIndex + sIndex) / 2)]
        
        i = sIndex
        j = eIndex
        
        while i < j :
            while mylist[i] < pivot and i <= j:
                i += 1
            
            while mylist[j] > pivot and j >= i:
                j -= 1
                
            if i < j:
                temp = mylist[i]
                mylist[i] = mylist[j]
                mylist[j] = temp
                i += 1
                j -= 1
            else:
                break
        
        
        if i == j:
            if mylist[i] <= pivot:
                quicksort(mylist, sIndex, i)
                quicksort(mylist, i + 1, eIndex)
            else:
                quicksort(mylist, sIndex, i - 1)
                quicksort(mylist, i, eIndex)
        else:
            quicksort(mylist, sIndex, j)
            quicksort(mylist, i, eIndex)
    # end else

a = [3, 6, 9, 2, 6, 8, 9, 1, 7, 21, 7, 12]

quicksort(a, 0, len(a) - 1)

print("After sorting: ", a)