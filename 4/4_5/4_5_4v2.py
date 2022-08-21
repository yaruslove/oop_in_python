from abc import ABC, abstractmethod
# from itertools import count

class Model(ABC):
    _counter = -1
    @abstractmethod
    def get_pk(self):
        '''Get primary key'''

    def get_info(self):
        return  "Базовый класс Model"

    @classmethod
    def gen_id(cls):
        cls._counter+=1
        return cls._counter


class ModelForm(Model):
    def __init__ (self,login, password):
        self._login = login
        self._password = password
        self._id=self.gen_id()

    def get_pk(self):
        return self._id


#### Test

form = ModelForm("Логин", "Пароль")
print(form.get_pk())

form1 = ModelForm("Логин", "Пароль")
print(form1.get_pk())

a=Model()
a.get_pk()


