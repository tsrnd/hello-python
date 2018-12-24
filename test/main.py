def divide(data,low,high): 
    i = ( low-1 )        
    pivot = data[high]     
  
    for j in range(low , high): 
  
        if   data[j] <= pivot: 
            i = i+1 
            data[i],data[j] = data[j],data[i] 
  
    data[i+1],data[high] = data[high],data[i+1] 
    return ( i+1 ) 
  
  
def quickSort(data,low,high): 
    if low < high: 
      i = divide(data,low,high) 
      quickSort(data, low, i-1) 
      quickSort(data, i+1, high)
    return data

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


def heapify(arr, n, i): 
    largest = i
    l = 2 * i + 1  
    r = 2 * i + 2 
  
    if l < n and arr[i] < arr[l]: 
        largest = l 
  
    if r < n and arr[largest] < arr[r]: 
        largest = r 
  
    if largest != i: 
        arr[i],arr[largest] = arr[largest],arr[i] 
        heapify(arr, n, largest) 
        
def heapSort(arr): 
  n = len(arr) 
  for i in range(n, -1, -1): 
      heapify(arr, n, i) 
  for i in range(n-1, 0, -1): 
      arr[i], arr[0] = arr[0], arr[i]
      heapify(arr, i, 0) 
  return arr
