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


def heapify(arr, n, i): 
    largest = i # Initialize largest as root 
    l = 2 * i + 1     # left = 2*i + 1 
    r = 2 * i + 2     # right = 2*i + 2 
  
    if l < n and arr[i] < arr[l]: 
        largest = l 
  
    if r < n and arr[largest] < arr[r]: 
        largest = r 
  
    if largest != i: 
        arr[i],arr[largest] = arr[largest],arr[i] # swap 
        heapify(arr, n, largest) 
        
def heapSort(arr): 
  n = len(arr) 
  for i in range(n, -1, -1): 
      heapify(arr, n, i) 
  for i in range(n-1, 0, -1): 
      arr[i], arr[0] = arr[0], arr[i] # swap 
      heapify(arr, i, 0) 
  return arr
