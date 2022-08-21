class TriangleListIterator:
    def __init__ (self,lst):
        self.lst=lst
        self.indx_x=-1
        self.indx_y=-1

    def __iter__ (self):
        self.indx_x=-1
        self.indx_y=-1
        return self
    def __next__ (self):
        if self.indx_x+1>self.indx_y:
            self.indx_y+=1
            self.indx_x=0
        else:
            self.indx_x+=1
        if self.indx_x==0 and self.indx_y+1>len(self.lst):
            raise StopIteration
       
        return self.lst[self.indx_y][self.indx_x]


# a= [["00","01","02","03","04"],
#     ["10","11","12","13","14"],
#     ["20","21","22","23","24"],
#     ["30","31","32","33","34"]]

a = [['x00', 'x01', 'x02'],
       ['x10', 'x11'],
       ['x20', 'x21', 'x22', 'x23', 'x24'],
       ['x30', 'x31', 'x32', 'x33']]

it = TriangleListIterator(a)

for x in it:  # последовательный перебор всех элементов списка: x00, x10, x11, x20, ...
    print(x)


it_iter = iter(it)
x = next(it_iter)