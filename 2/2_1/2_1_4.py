class Line:
    def __init__ (self,x1, y1, x2, y2):
        self.set_coords(x1, y1, x2, y2)
        
    def set_coords(self,x1, y1, x2, y2):
        if self.__check_value(x1):
            self.__x1=x1
        if self.__check_value(x2):
            self.__x2=x2
        if self.__check_value(y1):
            self.__y1=y1
        if self.__check_value(y2):
            self.__y2=y2 
    def get_coords(self):
        return (self.__x1,self.__y1,self.__x2,self.__y2)
            
    
    @classmethod
    def __check_value(cls, val):
        return type(val) in (float,int)
    
    def draw(self):
        print(f"{self.__x1} {self.__y1} {self.__x2} {self.__y2}")