import exam_module_validate as validate
def greeting(name):
    print("Hello, " + name)


def checkUser(username):
    #Validate length
    if validate.checkLength(username) == False: return False
    if validate.checkDigit(username) == True: return False
    return True;
    

