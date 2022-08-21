
class Car:
    def __init__(self):
        self.__model=""
        
        
    @property
    def model(self):
        return self.__model
    
    @model.setter
    def model(self,value):
        if isinstance(value,str) and 2<=len(value)<=100:
            self.__model=value
        
car = Car()


