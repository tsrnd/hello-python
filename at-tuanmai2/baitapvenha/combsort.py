def combsort(array):
    space = len(array) - 1
    haveChange = True
    while space > 1 and not haveChange:
        haveChange = False
        for i in range(0, len(array) - space - 1):
            if array[i] > array[i + space]:
                array[i], array[i + space] = array[i + space], array[i]
                haveChange = True
        if space > 1:
            space -= 1
    return array

