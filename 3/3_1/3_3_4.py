


class Museum:
    def __init__ (self,name):
        self.name=name
        self.exhibits=list()
        
    def add_exhibit(self, obj):
        self.exhibits.append(obj)
        
    def remove_exhibit (self, obj):
        self.exhibits.remove(obj)
        
    def get_info_exhibit(self,indx):
        return f"Описание экспоната {self.exhibits[indx].name}: {self.exhibits[indx].descr}"
    
class Picture:
    def __init__ (self,name,author,descr):
        self.name=name
        self.author=author
        self.descr=descr
        
class Mummies:
    def __init__ (self,name,location,descr):
        self.name=name
        self.location=location
        self.descr=descr

class Papyri:
    def __init__ (self,name,date,descr):
        self.name=name
        self.date=date
        self.descr=descr
        
  

