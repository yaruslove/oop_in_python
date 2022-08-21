from typing import Union

class Budget:
    def __init__ (self):
        self.__lst_expense=list()
    def add_item(self,it):
        self.__lst_expense.append(it)
    def remove_item(self, indx):
        if len(self.__lst_expense)>=indx+1:
            del self.__lst_expense[indx]
    def get_items(self):
        return self.__lst_expense


class Item:
    def __init__ (self,name, money):
        self.name: str=name
        self.money: Union[int, float]=money

    def __add__ (self, another):
        if type(another)==Item:
            return self.money+another.money
        elif type(another) in (int,float):
            return self.money+another

    def __radd__ (self, another):
        return self+another

# a=  Item("ogon",12)
# b=  Item("riba",10)
# c=  Item("potato",1)  
# print(a+c+b)

my_budget = Budget()
my_budget.add_item(Item("Курс по Python ООП", 2000))
my_budget.add_item(Item("Курс по Django", 5000.01))
my_budget.add_item(Item("Курс по NumPy", 0))
my_budget.add_item(Item("Курс по C++", 1500.10))

# print(my_budget.get_items())

# вычисление общих расходов
s = 0
for x in my_budget.get_items():
    s = s + x
print(s)
