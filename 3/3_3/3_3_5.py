import math


class Complex:
    def __init__ (self,real, img):
        self.real=real
        self.img=img
    
    @property
    def real (self):
        return self.__real
    @real.setter
    def real (self,value):
        if isinstance(value, (int,float)):
            self.__real=value
        else:
            raise ValueError("Неверный тип данных.")

    @property
    def img (self):
        return self.__img
    @img.setter
    def img (self,value):
        if isinstance(value, (int,float)):
            self.__img=value
        else:
            raise ValueError("Неверный тип данных.")

    def __abs__ (self):
        return math.sqrt(self.__real**2 + self.__img**2)

cmp = Complex(real = 7, img = 8)

cmp.real=3
cmp.img=4

c_abs=abs(cmp)