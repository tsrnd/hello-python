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