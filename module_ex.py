from function import myfunc, Hello
import function as f  # Rename a module us `as` keyword

myfunc("maitrabm")
#output ['m', 'i', 't', 'r']

Hello()

f.Summation().sum(1, 2)
# output 3


func = f.profile("tram", 23)
func.info()
# output
# Your name is:  tram
# Your age is:  23
