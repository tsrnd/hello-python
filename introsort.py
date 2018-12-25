#!/usr/bin/python
import math


def introSort(alist):
    maxdepth = (len(alist).bit_length() - 1)*2
    introsort_helper(alist, 0, len(alist), maxdepth)
    return


def introsort_helper(alist, start, end, maxdepth):
    if end - start <= 1:
        return
    elif maxdepth == 0:
        heapsort(alist, start, end)
    else:
        p = partition(alist, start, end)
        introsort_helper(alist, start, p + 1, maxdepth - 1)
        introsort_helper(alist, p + 1, end, maxdepth - 1)
    return


def partition(alist, start, end):
    pivot = alist[start]
    i = start - 1
    j = end

    while True:
        i = i + 1
        while alist[i] < pivot:
            i = i + 1
        j = j - 1
        while alist[j] > pivot:
            j = j - 1

        if i >= j:
            return j
        alist[i], alist[j] = alist[j], alist[i]
    return


def heapsort(alist, start, end):
    build_max_heap(alist, start, end)
    for i in range(end - 1, start, -1):
        alist[i], alist[start] = alist[start], alist[i]
        max_heapify(alist, index=0, start=start, end=i)
    return


def build_max_heap(alist, start, end):
    def parent(i):
        return (i - 1)//2
    length = end - start
    index = parent(length - 1)
    while index >= 0:
        max_heapify(alist, index, start, end)
        index = index - 1


def max_heapify(alist, index, start, end):
    def left(i):
        return 2*i + 1

    def right(i):
        return 2*i + 2

    size = end - start
    l = left(index)
    r = right(index)
    if (l < size and alist[start + l] > alist[start + index]):
        largest = l
    else:
        largest = index
    if (r < size and alist[start + r] > alist[start + largest]):
        largest = r
    if largest != index:
        alist[start + largest], alist[start +
                                      index] = alist[start + index], alist[start + largest]
        max_heapify(alist, largest, start, end)
    return
