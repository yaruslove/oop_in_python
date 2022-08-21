def chck_val(s,v):
    if not (s.cb and v.cb):
        raise ValueError("Неизвестен курс валют.")

def eq(s,v):
    chck_val(s,v)
    return round(s.volume/s.cb.rates[str(s)], 1) ==round(v.volume/v.cb.rates[str(v)],1)
def lt(s,v):
    chck_val(s,v)
    return round(s.volume/s.cb.rates[str(s)], 1) < round(v.volume/v.cb.rates[str(v)],1)
def le(s,v):
    chck_val(s,v)
    return round(s.volume/s.cb.rates[str(s)], 1) <= round(v.volume/v.cb.rates[str(v)],1)
    
class MoneyR:
    def __init__ (self,balance=0):
        self.__volume=balance
        self.__cb=None
    
    def __str__ (self):
        return "rub"

    @property
    def cb(self):
        return self.__cb

    @cb.setter
    def cb(self,v):
        self.__cb=v

    @property
    def volume(self):
        return self.__volume

    @volume.setter
    def volume(self,v):
        self.__volume=v

    def __eq__(self,v):
        return eq(self,v)

    def __lt__(self,v):
        return lt(self,v)

    def __le__(self,v):
        return le(self,v)

    @property
    def ccr(self):
        return  self.__cb.rates


class MoneyD:
    def __init__ (self,balance=0):
        self.__volume=balance
        self.__cb=None

    def __str__ (self):
        return "dollar"

    @property
    def cb(self):
        return self.__cb

    @cb.setter
    def cb(self,v):
        self.__cb=v

    @property
    def volume(self):
        return self.__volume

    @volume.setter
    def volume(self,v):
        self.__volume=v

    def __eq__(self,v):
        return eq(self,v)
    def __lt__(self,v):
        return lt(self,v)
    def __le__(self,v):
        return le(self,v)

class MoneyE:
    def __init__ (self,balance=0):
        self.__volume=balance
        self.__cb=None

    def __str__ (self):
        return "euro"

    @property
    def cb(self):
        return self.__cb

    @cb.setter
    def cb(self,v):
        self.__cb=v

    @property
    def volume(self):
        return self.__volume

    @volume.setter
    def volume(self,v):
        self.__volume=v

    def __eq__(self,v):
        return eq(self,v)
    def __lt__(self,v):
        return lt(self,v)
    def __le__(self,v):
        return le(self,v)

class CentralBank:
    rates = {'rub': 72.5, 'dollar': 1.0, 'euro': 1.15}
    def __new__(cls, *args, **kwargs):
        return None

    @classmethod
    def register(cls, money):
        money.cb=cls
        

CentralBank.rates = {'rub': 50, 'dollar': 1.0, 'euro': 1.15}

d1 = MoneyD(800)
d2 = MoneyD(800.1005)

CentralBank.register(d1)
CentralBank.register(d2)

if d1 == d2:
    print("равны")
else:
    print("нужно поднажать")

