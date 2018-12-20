numberstr = 123456789
strConvert = str(numberstr)

# display sequense.
for i in range(0, len(strConvert)):
    print(strConvert[i])

# display reserve sequense
a = ''.join(str(i) for i in range(len(strConvert), 0, -1))
print(a)

# display sequense of odd number.
sequense = ''
for i in range(0, len(strConvert)):
    idOdd = int(strConvert[i])
    if idOdd % 2 == 1:
        sequense += str(idOdd)
print(sequense)

# display sequense of even number.
sequense = ''
for i in range(0, len(strConvert)):
    idOdd = int(strConvert[i])
    if idOdd % 2 == 0:
        sequense += str(idOdd)
print(sequense)
