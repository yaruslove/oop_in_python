import sys

class DataBase:
    def __init__ (self,path):
        self.path:str = path
        self.dict_db=dict()

    def write(self, record):
        for i in self.dict_db:
            if i==record:
                self.dict_db[i].append(record)
                return None
        self.dict_db[record]=[record]

    def read(self, pk):
        for key, value in self.dict_db.items():
            for obj in value:
                if obj.pk==pk:
                    return obj



class  Record:
    __len_instances=0
    def __new__ (cls, *args, **kwargs):
        cls.__len_instances+=1
        return super().__new__(cls)
    def __init__ (self,fio, descr, old):
        self.fio:str =fio
        self.descr:str =descr
        self.old:int =int(old)
        self.pk=self.__len_instances

    def __hash__(self):
        return hash((self.fio.lower(),self.old))

    def __eq__ (self,v):
        return hash(self)==hash(v)

lst_in=["Балакирев С.М.; программист; 33",
"Кузнецов А.В.; разведчик-нелегал; 35",
"Суворов А.В.; полководец; 42",
"Иванов И.И.; фигурант всех подобных списков; 26",
"Балакирев С.М.; преподаватель; 37"]

# lst_in = list(map(str.strip, sys.stdin.readlines()))

db = DataBase('123')

for i in lst_in:
    fio, descr, old=i.split("; ")
    db.write(Record(fio, descr, old))

print(db.read(5).fio)
