class Chisla:
    @classmethod
    def verify_coord(cls, coord):
        if type(coord) not in (int,float):
            raise TypeError('координаты должны быть числами')
    def __set_name__(self, owner, name):
        self.name = "_" + name
 
    def __get__(self, instance, owner):
        return instance.__dict__[self.name]
 
    def __set__(self, instance, value):
        self.verify_coord(value)
        instance.__dict__[self.name] = value


class Track:
    def __init__ (self,*argums):
        self.__points=list(argums)

    def add_back(self, pt):
        self.__points.append(pt)

    def add_front(self, pt):
        self.__points.insert(0, pt)

    def pop_back(self):
        del self.__points[-1]

    def pop_front(self):
        del self.__points[1]

    @property
    def points(self):
        return tuple(self.__points)

class PointTrack:
    x = Chisla()
    y = Chisla()
    def __init__ (self,x, y):
        self.x = x
        self.y = y

    def __str__ (self):
        return f"PointTrack: {self.x}, {self.y}"

tr = Track(PointTrack(0, 112), PointTrack(1.2, -0.5), PointTrack(2.4, -1.5))
tr.add_back(PointTrack(1.4, 0))
tr.pop_front()
for pt in tr.points:
    print(pt)