try:
    a = open("abc.txt", "r")
    c = a.read()
    print(c)
except FileNotFoundError as e:
    print("File not found", e)
finally:
    print("finally")


class CustomError(RuntimeError):
    def __init__(self, arg):
        self.arg = arg


try:
    raise CustomError("File not found")
except CustomError as e:
    print(e.arg)
