class Aircraft:
    def __init__(self, model, mass, speed, top):
        self._model = model
        self._mass = mass
        self._speed = speed
        self._top = top

    def __setattr__(self, key, value):
        if key == '_model':
            if type(value) != str:
                raise TypeError('неверный тип аргумента')
        elif key in ('_mass', '_speed', '_top'):
            if not isinstance(value, (int, float)) or value <= 0:
                raise TypeError(f'неверный тип аргумента')
        object.__setattr__(self, key, value)

class PassengerAircraft(Aircraft):
    def __init__(self, model, mass, speed, top, chairs):
        super().__init__(model, mass, speed, top)
        self._chairs = chairs
        
    def __setattr__(self, key, value):
        if key == '_chairs':
            if type(value) != int or value <= 0:
                raise TypeError('неверный тип аргумента')
        super().__setattr__(key, value)


class WarPlane(Aircraft):
    def __init__(self, model, mass, speed, top, weapons):
        super().__init__(model, mass, speed, top)
        self._weapons = weapons
        
    def __setattr__(self, key, value):
        if key == '_weapons':
            if type(value) != dict:
                raise TypeError('неверный тип аргумента')
            else:
                for k, v in value.items():
                    if type(k) != str or type(v) != int:
                        raise TypeError('неверный тип аргумента')
        super().__setattr__(key, value)


planes = [PassengerAircraft('МС-21', 1250, 8000, 12000.5, 140), 
          PassengerAircraft('SuperJet', 1145, 8640, 11034, 80),
          WarPlane('Миг-35', 7034, 25000, 2000, {"ракета": 4, "бомба": 10}),
          WarPlane('Су-35', 7034, 34000, 2400, {"ракета": 4, "бомба": 7})]