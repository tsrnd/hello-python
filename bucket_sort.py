import insertion_sort

def sort(array, k):
    buckets = [[] for i in range(k)]
    M = max(array)
    for i in range(len(array)):
        buckets[int(array[i]/(M*k))].append(array[i])
    for i in range(k):
        insertion_sort.sort(buckets[i])

    result = []
    for bucket in buckets:
        result += bucket

    return result
