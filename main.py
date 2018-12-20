import MyModule.PracticCodeSyntax as M
from importlib import reload

M.isLucky(123)
M.isLucky(123)

reload(M)

print("This is name of Module M: ",M.__name__)
print("This is patch of Module M: ",M.__file__)
print("This is package of Module M: ",M.__package__)
print("This is list name Fuction of Module M: ",dir(M))

