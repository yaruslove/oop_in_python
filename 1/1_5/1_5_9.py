# здесь пишется программа


import random
random.seed(12345)

class Cell:
    def __init__ (self,around_mines,mine):
        self.around_mines=around_mines
        self.mine=mine
        self.fl_open=True

class GamePole:
    def __init__ (self,n,m):
        self.n=n
        self.m=m
        self.pole_2d=list()
        self.init()
        
    def init(self):
        lst_bl=[False for i in range(self.n*self.n)]
        for i in range(self.m):
            lst_bl[i]=True
        random.shuffle(lst_bl)
        myit = iter(lst_bl)
        for i in range(self.n):
            self.pole_2d.append(list())
            for j in range(self.n):
                self.pole_2d[i].append(next(myit))
        self.pole=self.create_pole_cells()
                
                
    def around_mines_func(self,x,y):
        tmp_list=list()
        for i in self.pole_2d[max(0, y-1):y+2]:
            tmp_list+=(i[max(0, x-1):x+2])
            mine=self.pole_2d[y][x]
        return sum(tmp_list)-int(mine),mine           
                
    def create_pole_cells(self):
        self.__pole_cells=list()
        for i in range(self.n):
            self.__pole_cells.append(list())
            for j in range(self.n):
                around_mines,mine=self.around_mines_func(j,i)
                
                self.__pole_cells[i].append(Cell(around_mines,mine))
        return self.__pole_cells
    
    def show(self):
        for i in range(self.n):
            tmp_str=str()
            for j in range(self.n):
                tmp_cell=self.__pole_cells[i][j]
                
                if tmp_cell.fl_open:
                    if tmp_cell.mine:
                        tmp_str+="*"
                    else:
                        tmp_str+=str(tmp_cell.around_mines)
                else:
                    tmp_str+="#"
            print(tmp_str)

pole_game=GamePole(10,12)

pole_game.show()