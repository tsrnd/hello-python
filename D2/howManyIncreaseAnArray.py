def arrayChange(inputArray):
    result = 0
    for i in range(1,len(inputArray)):
        if (inputArray[i] <= inputArray[i-1]) :
            a = inputArray[i-1] - inputArray[i] + 1
            result += a
            inputArray[i] += a
    return result
    
print(arrayChange([1,1,1]))