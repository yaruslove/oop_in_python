class Ellipse:
    def __init__ (self,x1=None, y1=None, x2=None, y2=None):
        if x1!=None and y1!=None and x2!=None and y2!=None:
            self.x1=x1
            self.y1=y1
            self.x2=x2
            self.y2=y2

    def __bool__ (self):
        if hasattr(self, 'x1'):
            return True
        else:
            return False

    def get_coords(self):
        if hasattr(self, 'x1'):
            return (self.x1, self.y1, self.x2, self.y2)
        else:
            raise AttributeError('нет координат для извлечения')

lst_geom=[Ellipse(),Ellipse(),Ellipse(1,2,3,4),Ellipse(5,6,7,8)]

for i in lst_geom:
    if i:
        i.get_coords()