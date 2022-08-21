from itertools import count
from abc import ABC, abstractmethod

class Model(ABC):
    _autoincrement = count()
    
    @abstractmethod
    def get_pk(self):
        '''Get primary key'''
        
    def get_info(self):
        return 'Базовый класс Model'
    
class ModelForm(Model):
    def __init__(self, login, password):
        self._id = next(self._autoincrement)
        self._login = login
        self._password = password
        
    def get_pk(self):
        return self._id

a=Model()
a.get_pk()