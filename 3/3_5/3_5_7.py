class Body:
    def __init__(self,name, ro, volume) -> None:
        self.name=name
        self.ro=float(ro)
        self.volume=float(volume)

    @property    
    def massa(self):
        return self.ro*self.volume
    
    def __eq__ (self,v):
        if isinstance(v,Body):
            v=v.massa
        return self.massa == v

    def __lt__ (self,v):
        if isinstance(v,Body):
            v=v.massa 
        return self.massa < v

body1=Body("Igor", "1", "2")
body2=Body("Igor", "2", "1")
print(body1 > body2)  # True, если масса тела body1 больше массы тела body2
print(body1 == body2) # True, если масса тела body1 равна массе тела body2
print(body1 < 10)     # True, если масса тела body1 меньше 10
print(body2 == 5 )