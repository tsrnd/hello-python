def printme( str ):
    if not str:
        print("empty")
    else:
        print(str)
    return
printme(str = "")

def printinfo( arg1, *vartuple ):
   print ("Output ")
   print (arg1)
   
   for var in vartuple:
      print (var)
   return
printinfo( 10 )
printinfo( 70, 60, 50 )

def sum(a,b):
    return a + b
print(sum(1,2))

sum = lambda a , b : a+b
print("Sum : %i vs %i : " %(10,20), sum(10,20))
