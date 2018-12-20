#if else
age = 15
if age > 17: 
  print("can see a rated R movie")
elif age < 17 and age > 12:
  print("can see a rated PG-13 movie")
else: 
  print("can only see rated PG movies")

if age>12:
      print("12")


#enumerate
presidents = ["Washington", "Adams", "Jefferson", "Madison", "Monroe", "Adams", "Jackson"]
for i in range(len(presidents)):
    print("in i ", i)
    print("President {}: {}".format(i + 1, presidents[i]))
    print("format", format(i+1))


presidents = ["Washington", "Adams", "Jefferson", "Madison", "Monroe", "Adams", "Jackson"]
for num, name in enumerate(presidents, start=1):
    print("nums",num)
    print("name",name)
    print("President {}: {}".format(num, name))

colors = ["red", "green", "blue", "purple"]
ratios = [0.2, 0.3, 0.1, 0.4]
# print("a",ratios)
for i, color in enumerate(colors):
    ratio = ratios[i]
    print("in i ", i)
    print("ratio", ratio)
    print("{}% {}".format(ratio * 100, color))
    
#zip
colors = ["red", "green", "blue", "purple"]
ratios = [0.2, 0.3, 0.1, 0.4]
for color, ratio in zip(colors, ratios):
    print("{}% {}".format(ratio * 100, color))

alist = ['a1', 'a2', 'a3']
for i, a in enumerate(alist):
    print(i, a)
#item
def capitalizeVowelsRegExp(input):
    substitutions = {
    'a' :  'A',
    'e' :  'E',
    'i' :  'I',
    'o' :  'O',
    'u' :  'U',
    'y' :  'Y',
  }
for before, after in substitutions.items():
    input =  input.replace(before, after)
return input


print(capitalizeVowelsRegExp("aasdsadasphu"))


#while
color = ["1","4","3"]
i = 0
while i < len(color):
    print(color[i])
    i += 1
print(range(len(color)))
print(len(color))

print(range(3))
for i in range(0,3):
    print("range", i)
    print(color[i])

for i in color:
    print(i)

#array
cars = ["Ford", "Volvo", "BMW"]
a = "phu"
[a]+cars
cars.append("Honda")
cars.insert(3,"Honda")
cars.pop(3)

print(cars)
