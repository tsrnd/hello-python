class Patient():
    def __init__(self, last_name, age): # __init__ là một contructor hay hàm dựng của class -- self tương tự các ngôn ngữ khác là this
        self.last_name = last_name
        self.age = age

    def say_if_minor(self):
        if self.age >21 :
            print ("this patient is a minor")

    def change_last_name(self, new_last_name):
        self.last_name = new_last_name

name = Patient("quoc", 22)

print (name.last_name)
name.change_last_name("void ng")

print (name.last_name)
