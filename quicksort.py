import random

def swap( x, y):
    t = x
    x = y
    y = t

def Rand(start, end, num): 
    res = [] 
    for j in range(num): 
        res.append(random.randint(start, end)) 
    return res 

def partition(arr,low,high): 
    i = ( low-1 )        
    pivot = arr[high]     
  
    for j in range(low , high): 
  
        if   arr[j] <= pivot: 
            i = i+1 
            arr[i],arr[j] = arr[j],arr[i] 
  
    arr[i+1],arr[high] = arr[high],arr[i+1] 
    return ( i+1 ) 
  
  
def quickSort(arr,low,high): 
    if low < high: 
      pi = partition(arr,low,high) 
      quickSort(arr, low, pi-1) 
      quickSort(arr, pi+1, high)
    return arr

listRandom = Rand(-100000,100000,10)
t = quickSort(listRandom, 0,9)
print(t)