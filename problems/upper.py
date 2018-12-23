string = 'hello world'
uppercase = ['u','e','o','a','i']
output = ''
for i in range(len(string)):
    if string[i] in uppercase:
        output += string[i].upper()
    else: output += string[i]
print(output)
