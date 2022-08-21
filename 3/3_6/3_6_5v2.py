
class Dimensions:
    def __init__(self, a, b, c):
        self.a = a if self.check(a) else 0
        self.b = b if self.check(b) else 0
        self.c = c if self.check(c) else 0
        
    def __hash__(self):
        return hash((self.a, self.b, self.c))
    
    @staticmethod
    def check(value):
        if value <= 0:
            raise ValueError("габаритные размеры должны быть положительными числами")
        return True
    def __repr__ (self):
        return f"(Cls Dimensions: {str(self.a)},{str(self.b)},{str(self.c)})"

s_inp="1 2 3; 4 5 6.78; 1 2 3; 3 1 2.5"
lst_dims = [Dimensions(*map(float, x.split())) for x in s_inp.split('; ')]

print("Before sort")
print(lst_dims)
print([hash(i) for i in lst_dims])
lst_dims.sort(key=hash)
print("\n")

print("After sort")
print(lst_dims)
print([hash(i) for i in lst_dims])


