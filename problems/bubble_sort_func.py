def buddle_sort(array):
    for i in range(len(array)-1, 0, -1):
        for j in range(i):
            if array[j] > array[j+1]:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp
    return array

# array = [1, 23, 4, 51, 7, 5, 8, 3, 6, 8, 235, 8, 23, 7346, 12]

# x = buddle_sort(array)
# print(x)
