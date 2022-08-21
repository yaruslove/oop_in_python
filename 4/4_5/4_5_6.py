from abc import ABC, abstractmethod

class CountryInterface(ABC):
    @property
    @abstractmethod
    def name(self):
        """Абстрактный объект-свойство"""

    @property
    @abstractmethod
    def population(self):
        """Абстрактный объект-свойство"""


    @property
    @abstractmethod
    def square(self):
        """Абстрактный объект-свойство"""

    @abstractmethod
    def get_info(self):
        """Метод для перемещения транспортного средства"""



class Country(CountryInterface):
    def __init__ (self, name, population, square):
        self._name, self.population, self.square=name, population, square

    @property
    def name(self):
        return self._name

    @property
    def population(self):
        return self._population

    @population.setter
    def population(self,v):
        if type(v)==int and v>0:
            self._population=v

    @property
    def square(self):
        return self._square

    @square.setter
    def square(self,v):
        if v>0:
            self._square=v

    def get_info(self):
        return f"{self.name}: {self.square}, {self.population}"

country = Country("Россия", 140000000, 324005489.55)
name = country.name
pop = country.population
country.population = 150000000
country.square = 354005483.0
print(country.get_info()) # Россия: 354005483.0, 150000000