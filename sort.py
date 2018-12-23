def insertionSort(inputArray):
    for x in range (1, len(inputArray)):
        a = inputArray[x]
        i = x
        while i > 0 and inputArray[i - 1] > a:
            inputArray[i] = inputArray[i - 1]
            i = i - 1
        inputArray[i] = a
    return inputArray

def bubbleSort(inputArray):
    for _ in range (0, len(inputArray)-2):
        for j in range(len(inputArray) - 1, 0, -1):
            if inputArray[j] < inputArray[j - 1]:
                tmp = inputArray[j]
                inputArray[j] = inputArray[j - 1]
                inputArray[j - 1] = tmp
    return inputArray
