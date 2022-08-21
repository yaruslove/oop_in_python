class DataDescriptor:
    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if self._check_value(value):
            setattr(instance, self.name, value)
        else:
            raise TypeError(f'Type of {self.name} is wrong')

    def _check_value(self, value):
        raise NotImplementedError

class ValuePositive(DataDescriptor):
    def _check_value(self, value):
        return isinstance(value, (int, float)) and value >= 0

class ValueIntPositive(DataDescriptor):
    def _check_value(self, value):
        return isinstance(value, int) and value >= 0

class ValueBool(DataDescriptor):
    def _check_value(self, value):
        return isinstance(value, bool)

class ValueStr(DataDescriptor):
    def _check_value(self, value):
        return isinstance(value, str)


class Food:
    name = ValueStr()
    weight = ValuePositive()
    calories = ValueIntPositive()

    def __init__(self, name, weight, calories):
        self.name = name
        self.weight = weight
        self.calories = calories

class BreadFood(Food):
    white = ValueBool()

    def __init__(self, name, weight, calories, white):
        super().__init__(name, weight, calories)
        self.white = white

class SoupFood(Food):
    dietary = ValueBool()

    def __init__(self, name, weight, calories, dietary):
        super().__init__(name, weight, calories)
        self.dietary = dietary

class FishFood(Food):
    fish = ValueStr()

    def __init__(self, name, weight, calories, fish):
        super().__init__(name, weight, calories)
        self.fish = fish