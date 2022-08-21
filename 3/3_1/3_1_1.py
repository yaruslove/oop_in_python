class Book:
    def __init__(self,title=str(),author=str(),pages=0,year=0):
        self.title=title
        self.author=author
        self.pages=pages
        self.year=year
    
    def  __setattr__ (self,key,value):
        if key=="title" and isinstance(value,str):
            object.__setattr__(self,key,value)
        elif key=="author" and isinstance(value,str):
            object.__setattr__(self,key,value)
        elif key=="pages" and isinstance(value,int):
            object.__setattr__(self,key,value)
        elif key=="year" and isinstance(value,int):
            object.__setattr__(self,key,value)
        else:
            raise TypeError("Неверный тип присваиваемых данных.")
            
book = Book("Python ООП", "Сергей Балакирев", 123, 2022)