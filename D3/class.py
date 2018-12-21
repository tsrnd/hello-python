class Foo:
    def instance_bar(self, x):
        print("executing instance_bar(%s, %s)" % (self, x))
    #@classmethod
    def class_bar(cls, x):
        print("executing class_bar(%s, %s)" % (cls, x))
    #@staticmethod
    def static_bar(x):
        print("executing static_bar(%s)" % x)

foo = Foo()
foo.instance_bar(12)
foo.class_bar(12)
foo.static_bar('args')