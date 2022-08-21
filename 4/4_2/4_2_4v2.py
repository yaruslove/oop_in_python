class Tuple(tuple):
    def __add__(self,iter_obj):
        return Tuple(super().__add__(Tuple(iter_obj)))

a="Python"
a=Tuple(a)

b="OOP"
b=Tuple(b)

c=a+b
print("after")
print(c)
print(type(c))
