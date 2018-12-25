import random
RUN = 32


def insertionSortSmall(arr, left, right):

    for i in range(left + 1, right+1):

        temp = arr[i]
        j = i - 1
        while arr[j] > temp and j >= left:

            arr[j+1] = arr[j]
            j -= 1

        arr[j+1] = temp


def mergeSmall(arr, l, m, r):
    len1, len2 = m - l + 1, r - m
    left, right = [], []
    for i in range(0, len1):
        left.append(arr[l + i])
    for i in range(0, len2):
        right.append(arr[m + 1 + i])

    i, j, k = 0, 0, l
    # after comparing, we merge those two array
    # in larger sub array
    while i < len1 and j < len2:

        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1

        else:
            arr[k] = right[j]
            j += 1

        k += 1

    # copy remaining elements of left, if any
    while i < len1:

        arr[k] = left[i]
        k += 1
        i += 1

    # copy remaining element of right, if any
    while j < len2:
        arr[k] = right[j]
        k += 1
        j += 1


def timSort(arr, n):
    for i in range(0, n, RUN):
        insertionSortSmall(arr, i, min((i+31), (n-1)))

    size = RUN
    while size < n:
        for left in range(0, n, 2*size):
            mid = left + size - 1
            right = min((left + 2*size - 1), (n-1))

            mergeSmall(arr, left, mid, right)

        size = 2*size
    return
    