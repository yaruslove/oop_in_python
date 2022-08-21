

class LinkedList:
    def __init__(self):
        self.__main_list=list()
    def add_obj(self, obj):
        if self.__main_list!=[]:
            prev_obj=self.__main_list[-1]
            obj.set_prev(prev_obj) # кидаем ссылку на предыдущий объект вновь добавляемуму
            prev_obj.set_next(obj) # кидаем ссылку на последующий (текущь) объектпредыдущему объекту
            
            self.__main_list.append(obj)
        else:
            self.__main_list.append(obj)
    def remove_obj(self):
        self.__main_list=self.__main_list[:-1]
        
    def get_data(self):
        return [i.get_data() for i in  self.__main_list]
    
    @property
    def head(self):
        if len(self.__main_list)==0:
            return None    
        return self.__main_list[0]
    
    @property
    def tail(self):
        if len(self.__main_list)==0:
            return None    
        return self.__main_list[-1]
        


class ObjList:
    def __init__(self,data):
        self.__next=None
        self.__prev=None
        self.__data=data
    
    def set_next(self, obj):
        self.__next=obj
    def set_prev(self, obj):
        self.__prev=obj
    def get_next(self):
        return self.__next
    def get_prev(self):
        return self.__prev
    def set_data(self, data):
        self.__data=data
    def get_data(self):
        return self.__data

ob = ObjList("данные 1")
lst = LinkedList()