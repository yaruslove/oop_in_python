from random import sample
from itertools import product

class Cell:
    def __init__ (self):
        self.__is_mine=False
        self.__number=0
        self.__is_open=False

    @property
    def is_mine(self):
        return self.__is_mine
   
    @is_mine.setter
    def is_mine(self,v):
        if type(v)==bool:
            self.__is_mine=v
        else:
            raise ValueError("недопустимое значение атрибута")

    @property
    def number(self):
        return self.__number
   
    @number.setter
    def number(self,v):
        if 0<=v<=8:
            self.__number=v
        else:
            raise ValueError("недопустимое значение атрибута")

    @property
    def is_open(self):
        return self.__is_open
   
    @is_open.setter
    def is_open(self,v):
        if type(v)==bool:
            self.__is_open=v
        else:
            raise ValueError("недопустимое значение атрибута")
    
    def __bool__ (self):
        return not self.is_open

    def __repr__(self):
        if self.is_mine:
            return "*"
        else:
            return str(self.number)
    
    def __str__(self):
        if self.is_mine:
            return "*"
        else:
            return str(self.number)




class GamePole:
    __len_instances=0
    def __new__(cls, *args, **kwargs):
        if cls.__len_instances==0:
                cls.__len_instances+=1
                cls.__instance_repeat=super().__new__(cls)
                return cls.__instance_repeat
        else:
            return cls.__instance_repeat
    def __init__ (self,N, M, total_mines):
        self.N, self.M = N, M
        self.total_mines=total_mines


    def init_pole(self):
        # генерим произвольное расположение мин
        mine_coords = sample([*product(range(self.N), range(self.M))], self.total_mines)
        self.__pole_cells= [[Cell() for _ in range(self.M)] for _ in range(self.N)]
        # print(self.__pole_cells)
        for x, y in mine_coords:
            self.__pole_cells[x][y].is_mine = True

        steps = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
        for x, y in product(range(self.N), range(self.M)):
            for st_x, st_y in steps:
                # print(f"0< x + st_x = {x + st_x}<self.M= {self.M},  0 <= y + st_y {y + st_y} < self.N ={self.N } ")
                if 0 <= x + st_x < self.N and 0 <= y + st_y < self.M and self.__pole_cells[x + st_x][y + st_y].is_mine:
                    self.__pole_cells[x][y].number += 1
    @property
    def pole(self):
        return self.__pole_cells
    
    def show_pole(self):
        for i in self.__pole_cells:
            for j in i:
                print(j, end=" ")
            print("\n")

    def open_cell(self,i, j):
        if 0 <= i < self.N and 0 <= j < self.M:
            self.__pole_cells[i][j].is_open=True
        else:
            raise IndexError('некорректные индексы i, j клетки игрового поля')

# pole = GamePole(20, 8, 10)
# pole.init_pole()
# pole.show_pole()

# pole = GamePole(10, 20, 10)  # создается поле размерами 10x20 с общим числом мин 10
# pole.init_pole()
# print(1)
# print(bool(pole.pole[0][1]))
# if pole.pole[0][1]:
#     print("here1")


# print(2)
# pole.open_cell(0, 1)
# print(bool(pole.pole[0][1]))
# if pole.pole[0][1]:
#     print("here2")


# if pole.pole[3][5]:
#     pole.open_cell(3, 5)
# pole.open_cell(30, 100)  # генерируется исключение IndexError
# pole.show_pole()


pole = GamePole(10, 20, 10)  # создается поле размерами 10x20 с общим числом мин 10
pole.init_pole()
print(bool(pole.pole[0][1]))
if pole.pole[0][1]:
    pole.open_cell(0, 1)
    print(bool(pole.pole[0][1]))
if pole.pole[3][5]:
    pole.open_cell(3, 5)