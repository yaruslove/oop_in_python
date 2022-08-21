# здесь объявляйте класс SingletonFive
class SingletonFive:
    __len_instances=0
    __instance_five=0
    def __new__(cls, *args, **kwargs):
        if cls.__len_instances<4:
            cls.__len_instances+=1
            return super().__new__(cls)
        if cls.__len_instances==4: 
            cls.__instance_five=super().__new__(cls)
            cls.__len_instances+=1
            return cls.__instance_five
        if cls.__len_instances>=5:
            return cls.__instance_five
    def __init__(self,data):
        self.name=data


objs = [SingletonFive(str(n)) for n in range(10)] # эту строчку не менять




