class ListInteger(list):
    def __init__(self, lst):
        if all([type(i)==int for i in lst]):
            super().__init__(lst)
        else:
            raise TypeError('можно передавать только целочисленные значения')
    def  __setitem__(self,key,value):
        if type(value) == int:
            super().__setitem__(key,value)
        else:
            raise TypeError('можно передавать только целочисленные значения')

    def append (self,value):
        if type(value) == int:
            super().append(value)
        else:
            raise TypeError('можно передавать только целочисленные значения')


# s = ListInteger((1, 2, 3))
# s[1] = 10
# s.append(11)
# print(s)
# print(s.lst)
# s[0] = 10.5 
