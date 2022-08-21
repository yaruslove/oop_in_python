class Track:
    def __init__(self,start_x, start_y) -> None:
        self.start_x=start_x
        self.start_y=start_y
        self.lst_crds=[]
    def add_point(self,x, y, speed):
        self.lst_crds.append([x, y, speed])

    def __getitem__ (self,indx):
        if not (type(indx)==int and 0<=indx<=len(self.lst_crds)-1):
            raise IndexError('некорректный индекс')
        x,y,speed=self.lst_crds[indx]
        return (x,y),speed

    def __setitem__ (self,indx,value):
        if not (type(indx)==int and 0<=indx<=len(self.lst_crds)-1):
            raise IndexError('некорректный индекс')
        self.lst_crds[indx][2]=value


tr = Track(10, -5.4)
print(tr.lst_crds)
tr.add_point(20, 0, 100) # первый линейный сегмент: indx = 0
print(tr.lst_crds)
tr.add_point(50, -20, 80) # второй линейный сегмент: indx = 1
print(tr.lst_crds)
tr.add_point(63.45, 1.24, 60.34) # третий линейный сегмент: indx = 2
print(tr.lst_crds)

tr[2] = 60
print(tr.lst_crds)
c, s = tr[2]
print(c, s)

res = tr[3] # IndexError