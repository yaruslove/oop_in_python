
class ItemAttrs:
    def __init__(self,*argums):
        self.l=list(argums)

    def __getitem__(self,k):
        return self.l[k]

    def __setitem__(self,k,v):
        self.l[k]=v

class Point(ItemAttrs):
    pass

pt = Point(1, 2.5)
x = pt[0]   # 1
y = pt[1]   # 2.5
pt[0] = 10