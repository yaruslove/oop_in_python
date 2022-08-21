from typing import Union

class Dimensions:
    def __init__ (self,a, b, c):
        self.a:Union(int,float) =self.check_numb(a)
        self.b:Union(int,float) =self.check_numb(b)
        self.c:Union(int,float) =self.check_numb(c)
    def __hash__ (self):
        return hash((self.a,self.b,self.c))
    def __repr__ (self):
        return f"(Cls Dimensions: {str(self.a)},{str(self.b)},{str(self.c)})"

    @staticmethod
    def check_numb(NumberString):
        if isinstance(NumberString,str):
            if NumberString.isdigit():
                Number = int(NumberString)
            else:
                Number = float(NumberString)
            if Number<=0:
                raise ValueError("габаритные размеры должны быть положительными числами")
            return Number

s_inp="1 2 3; 4 5 6.78; 1 2 3; 3 1 2.5"
lst_dims=[]
for i in s_inp.split("; "):
    a, b, c = i.split(" ")
    lst_dims.append(Dimensions(a, b, c))

print("Before sort")
print(lst_dims)
print([hash(i) for i in lst_dims])
lst_dims = sorted(lst_dims, key=lambda x: hash(x))
print("\n")

print("After sort")
print(lst_dims)
print([hash(i) for i in lst_dims])
