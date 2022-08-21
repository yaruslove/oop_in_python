class IntegerValue:
    def __set_name__(self, owner, name):
        self.name = "_" + name
 
    def __get__(self, instance, owner):
        return instance.__dict__[self.name]
 
    def __set__(self, instance, value):
        if type(value)!=int:
            raise ValueError('возможны только целочисленные значения')
        instance.__dict__[self.name] = value


class CellInteger:
    value = IntegerValue()
    def __init__ (self,start_value=0):
        self.value = start_value

class TableValues:
    def __init__ (self, rows, cols, cell=None):
        if not cell:
            raise ValueError('параметр cell не указан')

        self._rows, self._cols = rows, cols

        self.cells=tuple([tuple([cell() for _ in range(self._cols)]) for _ in range(self._rows)])

    def __getitem__ (self,item):
        indx_1,indx_2 = item
        return self.cells[indx_1][indx_2].value

    def __setitem__ (self,item,value):
        indx_1,indx_2 = item
        self.cells[indx_1][indx_2].value=value

    def __repr__ (self):
        rtrn=str()
        for i in  self.cells:
            for j in i:
                rtrn+=f"{j} "
            rtrn+="\n"
        return rtrn



table = TableValues(2, 3, cell=CellInteger)
print(table[0, 1])
table[1, 1] = 10
# table[0, 0] = 1.45 # генерируется исключение ValueError

# вывод таблицы в консоль
for row in table.cells:
    for x in row:
        print(x.value, end=' ')
    print()