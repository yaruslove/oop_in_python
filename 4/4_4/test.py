class Auto:
    __MIN_WEIGHT = 100
    __MAX_WEIGHT = 1000

    def __init__(self, model):
        self.__verify_model(model)
        self.__model = model

    def __verify_model(self, model):
        if type(model) != str:
            raise TypeError('модель должна представляться строкой')

    def __verify_weight(self, weight):
        if self.__MIN_WEIGHT > weight or weight > self.__MAX_WEIGHT:
            raise TypeError(f'вес автомобиля BMW должен быть в пределах [{self.__MIN_WEIGHT}; {self.__MAX_WEIGHT}]')


class BMW(Auto):
    def __init__(self, model, weight):
        super().__init__(model)
        self.__verify_weight(weight)
        self.__weight = weight



bmw_x5 = BMW('BMW X5', 512.5)
print(bmw_x5._BMW__weight)
print(bmw_x5._Auto__model)