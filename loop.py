for i in range(1,10):
    if i == 5:
        continue
    elif i == 2:
        pass
        print(i)
    elif i == 9:
        break
    else:
        print(i)

list = [1,"a",2,"b",3,"c"]
for i in list:
    print(i)
else:
    print("finish")

count = 0
while count<7:
    print(count*count)
    count+=1
print("finish")
