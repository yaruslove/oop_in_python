class Bag:
    def __init__ (self,max_weight):
        self.max_weight=max_weight
        self.__crnt_weight=0
        self.__things=list()

    def add_thing(self,thing):
        tmp=self.__crnt_weight+thing.weight
        if tmp<=self.max_weight:
            self.__things.append(thing)
            self.__crnt_weight=tmp
        else:
            raise ValueError('превышен суммарный вес предметов')

    def checker(self,k):
        if type(k)==int and 0<=k<len(self.__things):
            return True
        else:
            raise IndexError('неверный индекс')

    def __setitem__ (self,k,v):
        self.checker(k)
        tmp=self.__crnt_weight-self.__things[k].weight+v.weight
        if tmp<=self.max_weight:
            self.__crnt_weight=tmp
            self.__things[k]=v
        else:
            raise ValueError('превышен суммарный вес предметов')

        

    def __getitem__ (self,k):
        self.checker(k)
        return self.__things[k]
    def __delitem__(self,k):
        self.checker(k)
        self.__crnt_weight-=self.__things[k].weight
        del self.__things[k]

    @property
    def weight(self):
        print(self.__crnt_weight)
        # return self.__crnt_weight



class Thing:
    def __init__  (self,name,weight):
        self.name, self.weight=name,weight

bag = Bag(1000)
print(1)
print(bag.weight)
bag.add_thing(Thing('книга', 100))
print(2)
print(bag.weight)
bag.add_thing(Thing('носки', 200))
print(3)
print(bag.weight)
bag.add_thing(Thing('рубашка', 500))
print(3)
print(bag.weight)
# bag.add_thing(Thing('ножницы', 300)) # генерируется исключение ValueError
print(bag[2].name) # рубашка
bag[1] = Thing('платок', 100)
print(bag[1].name) # платок
del bag[0]
print(bag[0].name) # платок
# t = bag[4] # генерируется исключение IndexError