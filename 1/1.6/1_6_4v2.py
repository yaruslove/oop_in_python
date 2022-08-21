class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def clone(self):
        new_clone = super().__new__(type(self))
        new_clone.__dict__.update(self.__dict__)
        return new_clone


pt = Point(1, 2)
pt_clone = pt.clone()