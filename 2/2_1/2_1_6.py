


class Point:
    def __init__(self,x,y):
        self.__set_coords(x,y)
    def __set_coords(self,x,y):
        if self.__check_value(x) and self.__check_value(y):
            self.__x,self.__y=x,y
    def get_coords(self):
        return (self.__x,self.__y)
    
    @classmethod
    def __check_value(cls, val):
        return type(val) in (float,int)

class Rectangle:
    def __init__(self, *args):
        if len(args)==2:
            self.__sp,self.__ep=args
        elif len(args)==4:
            self.__sp = Point(args[0],args[1])
            self.__ep = Point(args[2],args[3])
    def set_coords (self,sp,ep):
            self.__sp, self.__ep= sp,ep
    def get_coords(self):
        return  self.__sp, self.__ep
    def draw (self):
        sp,ep=self.get_coords()
        x1,y1=sp.get_coords()
        x2,y2=ep.get_coords()
        print(f"Прямоугольник с координатами: ({x1}, {y1}) ({x2}, {y2})")

        
rect = Rectangle( 0, 0, 20, 34)
