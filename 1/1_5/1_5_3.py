import random


class Figures:
    def __init__(self,a, b, c, d):
        self.sp=(a, b)
        self.ep=(c, d)

class Line(Figures):
    pass

class Rect(Figures):
    pass

class Ellipse(Figures):
    pass

elements=[]

for i in range(217):
    a,b=random.sample(range(101, 200), 2)
    c,d=random.sample(range(1, 100), 2)
    l,r,e=Line(a,b,c,d),Rect(a,b,c,d),Ellipse(a,b,c,d)
    figrs = [l,r,e]
    tmp=random.choice(figrs)

    if isinstance(tmp, Line):
        tmp=Line(0,0,0,0)

    elements.append(tmp)


    