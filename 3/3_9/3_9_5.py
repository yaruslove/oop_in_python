class Cell:
    def __init__ (self,data):
        self.__data=data
        self.tp=type(data)

    @property
    def data(self):
        return  self.__data

    @data.setter
    def data(self,d):
        if type(d)!=TableValues.type_data:
            raise TypeError('неверный тип присваиваемых данных')
        self.__data=d

class TableValues:
    type_data=int
    def __init__ (self, rows, cols, type_data=int):
        self.rows=rows
        self.cols=cols
        TableValues.type_data=type_data
        self.table=list()
        for y in range(rows):
            tmp_l=[]
            for x in range(cols):
                tmp_l.append(Cell(0))
            self.table.append(tmp_l)

    def check_xy (self, x,y):
        if (type(x)!=int or type(y)!=int) and 0 > x <= self.cols and 0 > y <= self.rows:
            raise IndexError('неверный индекс')
    def __getitem__ (self,pos):
        y,x = pos
        self.check_xy(x,y)
        return self.table[y][x].data
    def __setitem__ (self,pos,v):
        y,x = pos
        self.check_xy(x,y)
        self.table[y][x].data=v

    def __iter__ (self):
        self.indx_y=-1
        return self
    def __next__ (self):
        self.indx_y+=1
        if self.indx_y+1>len(self.table):
            raise StopIteration
        return [i.data for i in self.table[self.indx_y]]






lst = [[0,1,2,3,4],
       [5,6,7,8,9],
       [10,11,12,13,14],
       [15,16,17,18,19]]
# a=TableValues(3,6)
# print(a.table)

table = TableValues(4, 5, int)

table[0,0]=2

# for indx_y, row in enumerate(table):  # перебор по строкам
#     for indx_x, value in enumerate(row): # перебор по столбцам
#         print(lst[indx_y][indx_x])
#         value.data=lst[indx_y][indx_x]
#     print("\n")

# for indx_y, row in enumerate(table):  # перебор по строкам
#     for indx_x, value in enumerate(row): # перебор по столбцам
#         print(f"HERE {value} ")
#     print("\n")