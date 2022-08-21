class IterColumn:
    def __init__ (self, lst, column):
        self.lst=lst
        self.x=column
        self.y=-1

    def __iter__ (self):
        self.y=-1
        return self

    def __next__ (self):
        if self.y+1<len(self.lst):
             self.y+=1
             return  self.lst[self.y][self.x]
        else:
            raise StopIteration     


lst = [["00","01","02","03","04"],
       ["10","11","12","13","14"],
       ["20","21","22","23","24"],
       ["30","31","32","33","34"]]
        

it = IterColumn(lst, 1)

for x in it:  # последовательный перебор всех элементов столбца списка: x12, x22, ..., xM2
    print(x)
