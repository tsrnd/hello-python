def isPermutation(n, inputArray):
    for i in range(0, len(inputArray)-1):
        for j in range(i+1, len(inputArray)):
            if inputArray[i] > inputArray[j]:
                tmp = inputArray[i]
                inputArray[i] = inputArray[j]
                inputArray[j] = tmp
    return checkSequense(n, inputArray)


def checkSequense(n, inputArray):
    if inputArray[len(inputArray)-1] != n:
        return False

    print('here')
    for i in range(0, len(inputArray)-1):
        if inputArray[i]+1 != inputArray[i+1]:
            return False
    
    return True




def myMaxOfThree(a, b, c):
    if (a>=b and b>=c) :
        return a;
    elif (a<=b and b<=c):
        return c;
    else: return b;




def replaceFirstDigitRegExp(input):
    
    new_str = []
    for i in range(0, len(input)-1):
        if (input[i] < '9' and input[i] > '0'):
            new_str = input[:i] + "#" + input[i+1:]
            break
    return new_str

print(replaceFirstDigitRegExp("There are 12 points"))