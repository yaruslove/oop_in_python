import sys

# программу не менять, только добавить два метода
lst_in = list(map(str.strip, sys.stdin.readlines()))  # считывание списка строк из входного потока


class DataBase:
    lst_data = []
    FIELDS = ('id', 'name', 'old', 'salary')
    
    def insert(self,lst_in):
        for i in lst_in:
            self.lst_data.append(dict(map(lambda *args: args, self.FIELDS, i.split(" "))))
        
    def select(self,a,b):
        if b>len(self.lst_data):
            b=len(self.lst_data)
        return self.lst_data[a:b+1]


db = DataBase()
db.insert(lst_in)