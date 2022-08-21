class Array:
    def __init__ (self,max_length, cell):
        self.__max_length=max_length
        self.__cell=cell
        self.lst=[self.__cell() for _ in range(self.__max_length)]


    def __getitem__ (self,indx):
        if not (type(indx)==int, 0<=indx<self.__max_length):
            raise IndexError('неверный индекс для доступа к элементам массива')
        return self.lst[indx].value
    def __setitem__ (self,indx,x):
        if not (type(indx)==int, 0<=indx<self.__max_length):
            raise IndexError('неверный индекс для доступа к элементам массива')
        self.lst[indx].value=x

    def __repr__ (self):
        return " ".join(map(str, self.lst))


class Integer:
    def __init__ (self,start_value=0):
        if type(start_value)!=int:
            raise ValueError('должно быть целое число')
        self.__x=start_value
        # self.__x=None

    @property
    def value (self):
        return self.__x
    
    @value.setter
    def value (self,x):
        if type(x)!=int:
            raise ValueError('должно быть целое число')
        self.__x=x
    
    def __repr__ (self):
        return str(self.__x)

ar_int = Array(10, cell=Integer)
print(ar_int[3])
print(ar_int) # должны отображаться все значения массива в одну строчку через пробел
ar_int[1] = 10