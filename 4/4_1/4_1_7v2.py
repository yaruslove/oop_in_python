class Vector:
    curnt_types=(int,float)
    def __init__ (self, *argums):
        self.__check_type(argums)
        self.vector=argums

    def __check_type(self, coords):
        if not all([type(i) in self.curnt_types  for i in coords]):
            raise ValueError('координаты должны быть целыми числами')


    @staticmethod
    def __check_shape (v1,v2):
        if len(v1) != len(v2):
            raise TypeError('размерности векторов не совпадают')

    def __swither_answer(self,coords):
        try:
            return self.__class__(*coords)
        except ValueError:
            return Vector(*coords)

    def __add__(self, v):
        self.__check_shape(self.vector, v.vector)
        coords= tuple([x + y for x, y in zip(self.vector, v.get_coords())])
        return self.__swither_answer(coords)

    def __sub__(self, v):
        self.__check_shape(self.vector, v.vector)
        coords = [x - y for x, y in zip(self.vector, v.get_coords())]
        return self.__swither_answer(coords)

    def get_coords(self):
        return tuple(self.vector)


class VectorInt (Vector):
    curnt_types=(int,)


v1 = VectorInt(1, 2, 3.4, 4)
v2 = VectorInt(1, 4, 3, 4)

a = v1-v2
print("type(a)",type(a))
print(a.vector)
print(a.get_coords())
