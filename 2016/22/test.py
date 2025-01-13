class Foo(tuple):

    def __new__ (cls, _, b):
        return super(Foo, cls).__new__(cls, tuple(b))

    def __init__(self, a, b):
        print(self)
        print("dict",self.__dict__)
        self.a = a
        print("__init__",a,b)
        print(self)
        print("dict",self.__dict__)


print(Foo(1,[2,3]))

a = ((1,2),(3,4))
b = a
b = ((11,22),)+a[1:]

print(a,b)