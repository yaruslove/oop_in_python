class Vector:
    def __init__ (self, *argums):
        self.vector=argums

    @staticmethod
    def __check_shape (v1,v2):
        if len(v1) != len(v2):
            raise TypeError('размерности векторов не совпадают')

    def __swither_answer(self,coords):
        print("__swither_answer coords",coords)
        try:
            return self.__class__(*coords)
        except ValueError:
            return Vector(*coords)

    def __add__(self, v):
        self.__check_shape(self.vector, v.vector)
        # print("self.vector",self.vector)
        # print("v.get_coords",v.get_coords())

        coords= tuple([x + y for x, y in zip(self.vector, v.get_coords())])
        return self.__swither_answer(coords)

    def __sub__(self, v):
        self.__check_shape(self.vector, v.vector)
        coords = [x - y for x, y in zip(self.vector, v.get_coords())]
        return self.__swither_answer(coords)

    def get_coords(self):
        return self.vector


class VectorInt (Vector):
    def __init__ (self, *argums):
        # a=[int == type(i) for i in argums]
        if not all([int == type(i) for i in argums]):
            raise ValueError('координаты должны быть целыми числами')
        self.vector=argums



# v2 = VectorInt(1, 0.2, 3, 4)

v1 = Vector(1, 2, 3, 4)
print(v1.vector)
v2 = VectorInt(1, 4, 3, 4)

a = v1+v2
print(a.vector)
print(a.get_coords())
