str = "Hello, World! "
print(str[1])
print(str.strip())
print(len(str))
print(str.lower())
print(str.upper())
print(str.replace("H", "J"))
print(str.split(","))
str = "this is string example....wow!!!"
print(str.swapcase())
intab = "aeiou"
outtab = "12345"
tran = str.maketrans(intab, outtab)
print(str.translate(tran))
