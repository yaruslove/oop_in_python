class ListMath:
    def __init__(self,l=None) -> None:
        if l!=None:
            self.lst_math=[ i for i in l if type(i) in (int,float) ]
        else:
            self.lst_math=[]

    def __add__ (self, other):
        nl=list()
        for i in self.lst_math:
            nl.append(i+ other) 
        return ListMath(nl)

    def __radd__ (self, other):
        nl=list()
        for i in self.lst_math:
            nl.append(i+ other) 
        return ListMath(nl)

    def __iadd__ (self, other):
        nl=list()
        for i in self.lst_math:
            nl.append(i+ other) 
        return ListMath(nl)

 ######## Sub
    def __sub__ (self, other):
        nl=list()
        for i in self.lst_math:
            nl.append(i- other) 
        return ListMath(nl)

    def __rsub__ (self, other):
        nl=list()
        for i in self.lst_math:
            nl.append(other-i) 
        return ListMath(nl)

    def __isub__ (self, other):
        nl=list()
        for i in self.lst_math:
            nl.append(i- other) 
        return ListMath(nl)

 ######## mul
    def __mul__ (self, other):
        nl=list()
        for i in self.lst_math:
            nl.append(i * other) 
        return ListMath(nl)

    def __rmul__ (self, other):
        nl=list()
        for i in self.lst_math:
            nl.append(other * i) 
        return ListMath(nl)

    def __imul__ (self, other):
        nl=list()
        for i in self.lst_math:
            nl.append(i * other) 
        return ListMath(nl)


 ######## truediv
    def __truediv__ (self, other):
        nl=list()
        for i in self.lst_math:
            nl.append(i / other) 
        return ListMath(nl)

    def __truediv__ (self, other):
        nl=list()
        for i in self.lst_math:
            nl.append(other / i) 
        return ListMath(nl)

    def __iruediv__ (self, other):
        nl=list()
        for i in self.lst_math:
            nl.append(i / other) 
        return ListMath(nl)