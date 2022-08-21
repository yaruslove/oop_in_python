class Tuple(tuple):
    def __add__(self,iter_obj):
        end_tuple=[]
        for i in iter_obj:
            end_tuple.append(i)
        
        rtrn=tuple(self)+ tuple(end_tuple)
        return Tuple(rtrn)

a="Python"
a=Tuple(a)

b="OOP"
b=Tuple(b)

c=a+b
print("after")
print(c)
print(type(c))
