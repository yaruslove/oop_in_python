class WindowDlg:
    def __init__ (self,title,width,height):
        self.__title=title
        self.__width,self.__height =None,None
        self.width,self.height=width,height
        
    def show(self):
        tmp=f"{self.__title}: {self.__width}, {self. __height}"
        print(tmp)
        del tmp
        
    def __check(self,value):
        if 0<=value<=10000 and isinstance(value,int):
            return True
        else:
            return False
        
    @property
    def width(self):
        return self.__width
    @width.setter
    def width(self, value):
        if self.__check(value):
            if self.__width:
                self.show()
            self.__width = value

    @property
    def height(self):
        return self.__height
    @height.setter
    def height(self, value):
        if self.__check(value):
            if self.__height:
                self.show()
            self.__height = value

wnd = WindowDlg("veka", 10, 20)