class Note:
    __agreed_notes= ('до', 'ре', 'ми', 'фа', 'соль', 'ля', 'си')
    def __init__ (self,name, ton):
        self._name =name
        self._ton=ton

            
    @property
    def _name(self):
        return self.__name

    @_name.setter 
    def _name(self,v):
        if v in self.__agreed_notes:
            self.__name=v
        else:
            raise ValueError('недопустимое значение аргумента')

    @property
    def _ton(self):
        return self.__ton

    @_ton.setter
    def _ton(self,v):
        if type(v) == int and v in [-1,0,1]:
            self.__ton=v
        else:
            raise ValueError('недопустимое значение аргумента')
    
    def __repr__ (self):
        return f"{self._name} {self._ton}"



class Notes:
    __instance=None
    __slots__ = '_do', '_re', '_mi', '_fa', '_solt', '_la', '_si','_lst'
    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __del__ (self):
        Notes.__instance = None

    def __init__ (self):
        self._lst=[]
        __сyrillic_notes = ['до', 'ре', 'ми', 'фа', 'соль', 'ля', 'си']
        __slt = ('_do', '_re', '_mi', '_fa', '_solt', '_la', '_si',)
        for s,n in zip(__slt, __сyrillic_notes):
            # print(s,n)
            setattr(self, s, Note(n,0))
            self._lst.append(getattr(self, s))

    def __check_indx(self,key):
        if key>=0 and key>=len(self._lst):
            raise IndexError('недопустимый индекс')
        if key<0 and abs(key)-1>=len(self._lst):
            raise IndexError('недопустимый индекс')

    def __getitem__(self, key):
        self.__check_indx(key)
        return self._lst[key]
        

    def __setitem__(self, key, value):
        self.__check_indx(key)
        self._lst[key] = value


notes = Notes()

## Test
print(notes[2])

print(notes._lst)