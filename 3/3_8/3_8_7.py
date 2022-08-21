class TicTacToe:
    def __init__ (self):
        self.rez=3
        self.pole=tuple([tuple([Cell() for i in range(self.rez)]) for j in range(self.rez)])

    def __repr__ (self):

        s=str()
        for i in self.pole:
            st=str()
            for j in i:
                # st+=str(j.is_free)+" "
                st+=str(j.value)+" "
            s+= st + "\n"
        return s


    def clear (self):
        for r in self.pole:
            pt=list()
            for c in r:
                c.is_free=True
                c.value=0

    def checker (self,k):
        if type(k)!=tuple() and  len(k)!=2:
            raise IndexError('неверный индекс клетки')
        elif type(k[0])==slice and type(k[1])==int and 0<=k[1]<self.rez:
            return True
        elif type(k[1])==slice and type(k[0])==int and 0<=k[0]<self.rez:
            return True
        elif type(k[0])==type(k[1])==int and 0<=k[0]<self.rez and 0<=k[1]<self.rez:
            return True
        else:
            raise IndexError('неверный индекс клетки')

    def __setitem__(self,k,v):
        self.checker(k)
        r,c=k
        if self.pole[r][c]:
            self.pole[r][c].value=v
            self.pole[r][c].is_free=False
        else:
            raise ValueError('клетка уже занята')

    def __getitem__(self,k):
        self.checker(k)
        r,c=k
        if type(r)==slice:
            t=[]
            for i in self.pole:
                t.append(i[c].value)
            return tuple(t)
        elif type(c)==slice:
            return tuple(i.value for i in self.pole[r])
        else:
            return self.pole[r][c].value


    

class Cell:
    def __init__(self):
        self.is_free=True
        self.value=0

    def __bool__ (self):
        return self.is_free


game = TicTacToe()
game.clear()
game[0, 0] = 1
game[1, 0] = 2

# game[2, 2] = 2
print(game)

if game[0, 0] == 0:
    game[0, 0] = 2
v1 = game[0, :]  # 1, 0, 0
v2 = game[:, 0]  # 1, 2, 0
print(v1)
print(v2)