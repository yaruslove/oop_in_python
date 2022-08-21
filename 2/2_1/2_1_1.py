class Clock:
    def __init__ (self):
        self.__time=0
    def set_time(self,tm):
        if self.__check_time(tm):
            self.__time=tm
    def get_time(self):
        return self.__time
    def __check_time(self,tm):
        return isinstance(tm,int) and tm>=0 and tm<100000
clock=Clock()
clock.set_time(4530)