import random

class Cell:
    def __init__ (self):
        self.value=0

    def __bool__ (self):
        return not bool(self.value)

    def __repr__ (self):
        return str(self.value)


class TicTacToe:
    FREE_CELL = 0      # свободная клетка
    HUMAN_X = 1        # крестик (игрок - человек)
    COMPUTER_O = 2     # нолик (игрок - компьютер)
    def __init__(self):
        self.__win=0 # 0 - is_playing, 1 - human_win, 2 - pc_win, 3 - is_draw
        self.__n=3
        self.pole=tuple([tuple([Cell() for _ in range(self.__n)]) for _ in range(self.__n)])

    def human_go(self):
        if not self:
            return

        while True:
            y,x = map(int, input("Please type coords:  ").split())
            n=list(range(self.__n))
            if not(y in n) or  not (x in n):
                continue

            if self[y,x] == self.FREE_CELL:
                self[y,x] = self.HUMAN_X
                break

    def computer_go(self):
        if not self:
            return
        
        free_lst=[]
        n=list(range(self.__n))
        for y in n:
            for x in n:
                if self.pole[y][x].value == self.FREE_CELL:
                    free_lst.append((y,x))
        y,x = random.choice(free_lst)
        self.pole[y][x].value=self.COMPUTER_O


    def init(self):
        # self.pole=tuple([tuple([Cell() for _ in range(self.__n)]) for _ in range(self.__n)])
        # self.pole=list()
        for i in self.pole:
            for j in i:
                j.value=0
        self.__win = 0

    def show(self):
        print("_______")
        for i in self.pole:
            print(i)
        print("_______")

    def __check_indx (self,items):
        if type(items) not in (tuple,list) or len(items)!=2:
            raise IndexError('некорректно указанные индексы')
        y,x=items
        n=list(range(self.__n))
        if not(y in n) or  not (x in n):
            raise IndexError('некорректно указанные индексы')
        return y,x

    def __chck_win (self):
        for r in self.pole:
            if all(i.value==self.HUMAN_X for i in r):
                self.__win=1
                return
            elif all(i.value==self.HUMAN_X for i in r):
                self.__win=2
                return
        
        for c in range(self.__n):
            columns= [r[c] for r in self.pole]
            if all(cl.value == self.HUMAN_X  for cl in columns):
                self.__win = 1
                return
            if all(cl.value == self.COMPUTER_O  for cl in columns):
                self.__win = 2
                return

        diagnl= [i for i in range(self.__n)]

        # Моя взяла
        if all(self.pole[i][i].value == self.HUMAN_X for i in diagnl) or all(self.pole[i][-1 -i ].value == self.HUMAN_X for i in diagnl):
            self.__win = 1
            return

        # Твоя взяла
        if all(self.pole[i][i].value == self.COMPUTER_O for i in diagnl) or all(self.pole[i][-1 -i ].value == self.COMPUTER_O for i in diagnl):
            self.__win = 2
            return

        # Ничья
        chck_lst=[]
        for i in self.pole:
            for j in i:
                chck_lst.append(j.value!=self.FREE_CELL)
        if all(chck_lst):
            self.__win = 3

    def __getitem__ (self, items):
        y,x=self.__check_indx(items)
        return self.pole[y][x].value
    def __setitem__ (self, items, v):
        y,x=self.__check_indx(items)
        self.pole[y][x].value=v
        self.__chck_win()

    @property
    def is_human_win(self):
        return self.__win==1

    @property
    def is_computer_win(self):
        return self.__win==2

    @property
    def is_draw(self):
        return self.__win==3

    def __bool__ (self):
        return self.__win == 0 and self.__win not in (1,2,3)


game = TicTacToe()
game.init()
step_game = 0
while game:
    game.show()

    if step_game % 2 == 0:
        game.human_go()
    else:
        game.computer_go()

    step_game += 1


game.show()

if game.is_human_win:
    print("Поздравляем! Вы победили!")
elif game.is_computer_win:
    print("Все получится, со временем")
else:
    print("Ничья.")