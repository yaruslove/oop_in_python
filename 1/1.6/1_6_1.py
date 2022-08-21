class AbstractClass:
    def __new__(cls):
        pass
        # print("Вызов new")
        return "Ошибка: нельзя создавать объекты абстрактного класса"


obj = AbstractClass()


