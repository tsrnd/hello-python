print("Hello, this is Function")


def plus(a, b):
    return "{}+{}={}".format(a, b, int(a)+int(b))


def tru(a, b):
    return "{}-{}={}".format(a, b, int(a)-int(b))


def nhan(a, b):
    return "{}*{}={}".format(a, b, int(a)*int(b))


def chia(a, b):
    return "{}/{}={}".format(a, b, int(a)/int(b))


def calculator():
    a = input("Enter [interger] a: ")
    b = input("Enter [interger] b: ")
    operator = input("Enter operator: [+,-,*,/]: ")
    try:
        if operator == "+":
            print(plus(a, b))
        elif operator == "-":
            print(tru(a, b))
        elif operator == "*":
            print(nhan(a, b))
        elif operator == "/":
            print(chia(a, b))
        else:
            print("Operator not correct, please check agian !")
    except:
        print("Error Syntax, please check agian !")
    option = input("Do you want continues ? [Yes/No]: ")
    if str(option).upper() == "yes".upper():
        calculator()
    else:
        print("Good Bye")
        return


calculator()
