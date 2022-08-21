class Protists:
    def __init__ (self,name, weight, old):
        self.name, self.weight, self.old = name, weight, old

class Plants(Protists):
    pass

class Mosses(Plants):
    pass

class Flowering(Plants):
    pass

class Animals(Protists):
    pass

class Mammals(Animals):
    pass

class Human(Mammals):
    pass

class Monkeys(Mammals):
    pass

class Worms(Animals):
    pass

#########
class Monkey(Monkeys):
    pass

class Person(Human):
    pass

class Flower(Flowering):
    pass

class Worm(Worms):
    pass

lst_objs=[Monkeys( "мартышка", 30.4, 7),
            Monkeys( "шимпанзе", 24.6, 8),
            Person( "Балакирев", 88, 34),
            Person( "Верховный жрец", 67.5, 45),
            Flower( "Тюльпан", 0.2, 1),
            Flower( "Роза", 0.1, 2),
            Worm ("червь", 0.01, 1),
            Worm ("червь 2", 0.02, 1),]

lst_animals=[i for i in lst_objs if isinstance(i,Animals)]
lst_plants=[i for i in lst_objs if isinstance(i,Plants)]
lst_mammals=[i for i in lst_objs if isinstance(i,Mammals)]
