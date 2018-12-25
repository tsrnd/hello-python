def quickSort(array):
    less = []
    equal = []
    greater = []

    if len(array) > 1:
        pivot = array[0]
        for x in array:
            if x < pivot:
                less.append(x)
            if x == pivot:
                equal.append(x)
            if x > pivot:
                greater.append(x)
        return quickSort(less)+equal+quickSort(greater)
    else: 
        return array

def shellSort(alist):
    sublistcount = len(alist)//2
    while sublistcount > 0:
        for start_position in range(sublistcount):
            for i in range(start_position+sublistcount,len(alist),sublistcount):

                current_value = alist[i]
                position = i

                while position>=sublistcount and alist[position-sublistcount]>current_value:
                    alist[position]=alist[position-sublistcount]
                    position = position-sublistcount

                alist[position]=current_value

        sublistcount = sublistcount // 2
    return alist
