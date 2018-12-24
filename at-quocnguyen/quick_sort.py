"""
Quick Sort

1. chọn 1 trục
2. xác định con trỏ trái và phải
3. so sánh element con trỏ trái với element con trỏ phải 
4. Check if lElement < pivot and rElement > pivot:
    yes -> tăng bên trái con trỏ và giảm bên phải
    no -> đổi vị trí 2 lE and rE

5. when l >= r => hoán đổi con trỏ trái hoăc phải
6. lặp lại 1 -5 đến hết list

"""

import unittest
def quickSort(alist):
    quickSortHelper(alist, 0, len(alist)-1)
    return alist

def quickSortHelper(alist, first, last):
    if first<last:
        splitpoint = partition(alist, first, last)
        quickSortHelper(alist, first, splitpoint-1)
        quickSortHelper(alist, splitpoint+1, last)

def partition(alist, first, last):
    pivotvalue = alist[first]
    leftmark = first+1
    rightmark = last
    done = False

    while not done:
        while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
            leftmark = leftmark +1

        while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
            rightmark = rightmark -1

        if rightmark < leftmark:
            done = True
        else:
            temp = alist[leftmark]
            alist[leftmark] = alist[rightmark]
            alist[rightmark] = temp

    temp = alist[first]
    alist[first] =  alist[rightmark]
    alist[rightmark] = temp

    return rightmark

alist = [5,9,6,2,7,0]
print("alist = ", alist)
quickSort(alist)
print ("quick sort alist = ", alist)
