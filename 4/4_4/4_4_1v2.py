class Discriptor_animal:
    def __set_name__(self, owner, name):
        self.name = "__" + name
 
    def __get__(self, instance, owner):
        if instance is None:
            return property()
        return instance.__dict__[self.name]
 
    def __set__(self, instance, value):
        instance.__dict__[self.name] = value


class Animal:
    name = Discriptor_animal()
    kind = Discriptor_animal()
    old = Discriptor_animal()
    def __init__ (self,name: str, kind: str, old: int) -> None:
       self.name:str = name
       self.kind:str = kind 
       self.old:int = old

animals = [Animal('Васька', 'дворовый кот', 5), Animal('Рекс', 'немецкая овчарка', 8), Animal('Кеша', 'попугай', 3) ]
