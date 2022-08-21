class TriangleChecker:
    def __init__(self,a, b, c):
        self.a=a
        self.b=b
        self.c=c

    def is_triangle(self):
        l=[self.a,self.b,self.c]
        for i in l:
            if not (type(i) in (float, int)):
                return 1
        for i in l:
            if i<=0:
                return 1
        if not(self.a+self.b>self.c and self.a+self.c>self.b and self.b+self.c>self.a):
            return 2
        else:
            return 3


a, b, c = map(int, input().split())

tr = TriangleChecker(a, b, c)
print(tr.is_triangle())