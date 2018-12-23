input = "Hello World"
vowel = ['a', 'e', 'i', 'o', 'u', 'y']
result = ''

for i in range(len(input)):
    x = input[i]
    if x in vowel:
        x = x.upper()
    result += x
print(result)
