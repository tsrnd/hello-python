def swap(list, i, j):
    temp = list[i]
    list[i] =  list[j]
    list[j] = temp
    return

def old_even_sort(list):
    sorted = False
    while (not sorted) :
        sorted = True
        for i in range(0, len(list) - 1, 2):
            if list[i] > list[i+1]:
                swap(list, i, i+1)
                sorted = False

        for i in range(1, len(list) - 1, 2):
            if list[i] > list[i+1]:
                swap(list, i, i+1)
                sorted = False
    return

list = [1,3,4,5,2,21,66]
old_even_sort(list)
print (list)