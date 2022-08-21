from typing import Union

class Furniture:
    def __init__ (self,name, weight):
        self._name: str =  name # self.__verify_name(name)
        self._weight: Union[float, int] = weight # self.__verify_weight(weight)


    @staticmethod
    def __verify_name(v):
        if type(v) == str:
            return v
        else:
            raise TypeError('название должно быть строкой')

    @staticmethod
    def __verify_weight(v):
        if type(v) in (float,int) and v>0:
            return v
        else:
            raise TypeError('вес должен быть положительным числом')

    @staticmethod
    def __verify_tp(v):
        if type(v) == bool:
            return v
        else:
            raise TypeError('тип должен быть bool')

    @staticmethod
    def __verify_doors(v):
        if type(v) == int:
            return v
        else:
            raise TypeError('число дверей должно быть целым положительным числом')

    @staticmethod
    def __verify_height_square(v):
        if type(v) in (int,float) and v>0:
            return v
        else:
            raise TypeError('значение должно быть положительным числом')


    def __setattr__(self, key, value):
        if key == "_name":
            value= self.__verify_name(value)
            object.__setattr__(self, key, value)
        elif key == "_weight":
            value= self.__verify_weight(value)
            object.__setattr__(self, key, value)
        elif key == "_tp":
            value= self.__verify_tp(value)
            object.__setattr__(self, key, value)
        elif key == "_doors":
            value= self.__verify_doors(value)
            object.__setattr__(self, key, value)
        elif key in  ("_height","_square"):
            value= self.__verify_height_square(value)
            object.__setattr__(self, key, value)
        else:
            object.__setattr__(self, key, value)

    def get_attrs(self):
        return tuple([value  for key,value in self.__dict__.items() if key.startswith("_")])


class Closet(Furniture):
    def __init__ (self, name, weight, tp, doors):
        super().__init__(name, weight)
        self._tp: bool =  tp
        self._doors: int = doors

class Chair(Furniture):
    def __init__ (self, name, weight, height):
        super().__init__(name, weight)
        self._height: Union[float, int] =  height

class Table(Furniture):
    def __init__ (self, name, weight, height, square):
        super().__init__(name, weight)
        self._height: Union[float, int] =  height
        self._square: Union[float, int] =  square


cl = Closet('шкаф-купе', 342.56, True, 3)
chair = Chair('стул', 14, 55.6)
tb = Table('стол', 34.5, 75, 10)

# print(cl.__dict__)
print(tb.get_attrs())



