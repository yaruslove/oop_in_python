class Digit:
    def __init__ (self,value):
        if type(value) != (str):
            self.value=value
        else:
            raise TypeError('значение не соответствует типу объекта')

class Float(Digit):
    def __init__ (self,value):
        super().__init__(value)
        if type(value) == float:
            self.value=value
        else:
            raise TypeError('значение не соответствует типу объекта')

class Integer(Digit):
    def __init__ (self,value):
        super().__init__(value)
        if type(value) == int:
            self.value=value
        else:
            raise TypeError('значение не соответствует типу объекта')


class Positive(Digit):
    def __init__ (self,value):
        super().__init__(value)
        if  value > 0:
            self.value=value
        else:
            raise TypeError('значение не соответствует типу объекта')

class Negative(Digit):
    def __init__ (self,value):
        super().__init__(value)
        if  value < 0:
            self.value=value
        else:
            raise TypeError('значение не соответствует типу объекта')


class PrimeNumber(Integer, Positive):
    def __repr__ (self):
        return str(self.value)


class FloatPositive(Float, Positive):
    def __repr__ (self):
        return str(self.value)

digits = [PrimeNumber(3), PrimeNumber(1), PrimeNumber(4), FloatPositive(1.5), FloatPositive(9.2), FloatPositive(6.5),
          FloatPositive(3.5), FloatPositive(8.9)]



def posit(i):
    if isinstance(i, Positive):
        return True
    else:
        return False

lst_positive = list(filter(posit, digits))
print(lst_positive)

def flt(i):
    if isinstance(i, Float):
        return True
    else:
        return False

lst_float = list(filter(flt, digits))
print(lst_float)

