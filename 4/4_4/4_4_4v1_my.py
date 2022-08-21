class Aircraft:
    def  __init__ (self, model, mass, speed, top):
        self._model=model
        self._mass=mass
        self._speed=speed
        self._top=top


    def __setattr__(self, __name: str, __value) -> None:
        if __name == "_model" and type(__value) != str:
            raise TypeError('неверный тип аргумента')
        if __name in ("_mass", "_speed", "_top") and __value<=0:
            raise TypeError('неверный тип аргумента')
        if __name in ("_model","_mass", "_speed", "_top"):
            object.__setattr__(self, __name, __value)

        # PassengerAircraft
        if __name == "_chairs" and type(__value)==int and __value>0:
            object.__setattr__(self, __name, __value)
        elif __name == "_chairs":    
            raise TypeError('неверный тип аргумента')

        # WarPlane
        if __name == "_weapons" and type(__value)==dict:
            for k,v in __value.items():
                if type(k) == str and type(v) in (float,int):
                    pass
                else:
                    raise TypeError('неверный тип аргумента')
            object.__setattr__(self, __name, __value)
        elif __name == "_weapons":    
            raise TypeError('неверный тип аргумента')


class PassengerAircraft(Aircraft):
    def __init__ (self, model, mass, speed, top, chairs):
        super().__init__(model, mass, speed, top)
        self._chairs=chairs
    

class WarPlane(Aircraft):
    def __init__ (self, model, mass, speed, top, weapons):
        super().__init__(model, mass, speed, top)
        self._weapons=weapons


planes = [PassengerAircraft('МС-21', 1250, 8000, 12000.5, 140),
          PassengerAircraft('SuperJet', 1145, 8640, 11034, 80),
          WarPlane('Миг-35', 7034, 25000, 2000, {"ракета": 4, "бомба": 10}),
          WarPlane('Су-35', 7034, 34000, 2400, {"ракета": 4, "бомба": 7})]
