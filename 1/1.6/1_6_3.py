class DialogWindows:
    name_class = "DialogWindows"
    def __init__(self,name):
        self.name=str(name)
        


class DialogLinux:
    name_class = "DialogLinux"    
    def __init__(self,name):
        self.name=str(name)

TYPE_OS=1

# здесь объявляйте класс Dialog
class Dialog:
    def __new__(cls, name, *args, **kwargs):
        if TYPE_OS==1:
            return DialogWindows(name)
        else:
            return DialogLinux(name)