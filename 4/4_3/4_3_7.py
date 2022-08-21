class StringDigit(str):
    def __init__ (self,s):
        self.chkr(s)
        self.s=s

    def chkr (self,s):
        if not s.isdigit():
            raise ValueError("в строке должны быть только цифры")

    def __str__(self):
        return self.s

    def __add__(self,v):        
        self.chkr(v)
        return StringDigit(self.s+v)

    def __radd__(self,v):        
        self.chkr(v)
        return StringDigit(v+self.s)

sd = StringDigit("123")
print(sd)       # 123
sd = sd + "456" # StringDigit: 123456
sd = "789" + sd # StringDigit: 789123456
print(sd)
print(sd.__repr__())
# sd = sd + "12f" # ValueError
