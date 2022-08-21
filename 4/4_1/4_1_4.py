class Singleton:
    __created=False
    __instance_base=False
    def __new__(cls, *args, **kwargs):
        if cls == Singleton:
            if not cls.__instance_base:
                cls.__instance_base=object.__new__(cls)
            return cls.__instance_base


        if not cls.__created:
            cls.__created=super().__new__(cls)
        return cls.__created
    # def __init__(self):
    #     pass
    

class Game(Singleton):
    def __init__(self,name):
        if 'name' not in self.__dict__:
            self.name=name

obj1=Game("igra_1")
obj2=Game("igra_2")
print(obj1.name)
print(obj2.name)
