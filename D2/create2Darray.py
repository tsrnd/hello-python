def create2DArray(lengths):
    result = []
    for i in range(len(lengths)):
        temp=[]
        for j in range(lengths[i]):
            temp.append(j)
        result.append(temp)
    return result

n=[3,2]
# print(n[1])
result = []
for i in range(len(n)):
    temp=[]
    for j in range(n[i]):
        temp.append(j)
    result.append(temp)
print(result)