def capitalizeVowelsRegExp(input):
    lowercase = ['a','e','i','o','u','y']
    output = ''
    for i in range(len(input)):
        if (input[i] in lowercase) :
            output += (input[i].upper())
        else :
            output+= (input[i])
    return output
print(capitalizeVowelsRegExp('There are some words'))