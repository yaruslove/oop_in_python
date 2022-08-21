class Vector:
    def __init__ (self, *arg):
        self.arg=arg

    def __len__ (self):
        return len(self.arg)

    def __add__(self,v):
        if type(v)==Vector and len(self) == len(v):
            return Vector(*[z[0]+z[1] for z in zip(self.arg, v.arg)])
        elif type(v) in (int,float):
            return Vector(*[z+v for z in self.arg])
        else:
            raise ArithmeticError('размерности векторов не совпадают')


    def __iadd__(self,v):
        if type(v)==Vector and len(self)==len(v):
            self.arg=[z[0]+z[1] for z in zip(self.arg, v.arg)]
            return self
        elif type(v) in (int,float):
            self.arg=[z+v for z in self.arg]
            return self
        else:
            raise ArithmeticError('размерности векторов не совпадают')


    def __sub__(self,v):
        if type(v)==Vector and len(self)==len(v):
            return Vector(*[z[0]-z[1] for z in zip(self.arg, v.arg)])
        elif type(v) in (int,float):
            return Vector(*[z-v for z in self.arg])
        else:
            raise ArithmeticError('размерности векторов не совпадают')
    
    def __isub__(self,v):
        if type(v)==Vector and len(self)==len(v):
            self.arg=[z[0]-z[1] for z in zip(self.arg, v.arg)]
            return self
        elif type(v) in (int,float):
            self.arg=[z-v for z in self.arg]
            return self
        else:
            raise ArithmeticError('размерности векторов не совпадают')
    
    def __mul__ (self,v):
        if type(v)==Vector and len(self)==len(v):
            return Vector(*[z[0]*z[1] for z in zip(self.arg, v.arg)])
        elif type(v) in (int,float):
            return Vector(*[z*v for z in self.arg])
        else:
            raise ArithmeticError('размерности векторов не совпадают')
    
    def __eq__(self, v):
        if len(self) != len(v):
            raise ArithmeticError('размерности векторов не совпадают')
        return all([a == b for a ,b in zip(self.arg, v.arg)])

v1=Vector(1,2,3)
v2=Vector(4,5,6)
print(v1==v2)
print(v1)
print(v2)

print("Test1")
print((v1 + v2).arg) # суммирование соответствующих координат векторов
print((v1 - v2).arg) # вычитание соответствующих координат векторов
print((v1 * v2).arg) # умножение соответствующих координат векторов
print("")


print("Test1.5")
print(v1)
v1 += 10 # прибавление ко всем координатам вектора числа 10
print(v1)
print(v1.arg)
print("")

print("Test2")
v1=Vector(1,2,3)
v2=Vector(4,5,6)
print(v1)
v1 -= 10 # вычитание из всех координат вектора числа 10
print(v1)
print(v1.arg)
print("")



print("Test3")
v1=Vector(1,2,3)
v2=Vector(4,5,6)
print(v1)
v1 += v2
print(v1)
print(v1.arg)
print("")


print("Test4")
v1=Vector(1,2,3)
v2=Vector(4,5,6)
print(v2)
v2 -= v1
print(v2)
print(v2.arg)
print("")


print("Test5")

print(v1 == v2) # True, если соответствующие координаты векторов равны
print(v1 != v2) # True, если хотя бы одна пара координат векторов не совпадает

