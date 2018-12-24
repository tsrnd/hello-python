import random
def selectionSort(data, size):
  for i in range(0, size-1):
    m = i
    for j in range(i+1, size):
        if(data[j] < data[m]):
          m = j
    if(m!= i):
      t = data[i]
      data[i] = data[m]
      data[m] = t
  return data

def Rand(start, end, num): 
    res = [] 
    for j in range(num): 
        res.append(random.randint(start, end)) 
    return res 


listRandom = Rand(-100000,100000,20)
print(listRandom)
t = selectionSort(listRandom,20)
print(t)

