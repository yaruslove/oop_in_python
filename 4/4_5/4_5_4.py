from abc import ABC, abstractmethod

class Model:
    @abstractmethod
    def get_pk(self):
        pass

    def get_info(self):
        return  "Базовый класс Model"


class ModelForm(Model):
    __cls_id=-1
    def __new__(cls, *args, **kwargs):
        cls.__cls_id+=1
        return super().__new__(cls)
    def __init__ (self,login, password):
        self._login, self._password=login, password
        self._id=self.__cls_id

    def get_pk(self):
        return self._id


#### Test

form = ModelForm("Логин", "Пароль")
print(form.get_pk())

