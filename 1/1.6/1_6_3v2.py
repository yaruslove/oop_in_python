TYPE_OS = 1 # 1 - Windows; 2 - Linux

class DialogWindows:
    name_class = "DialogWindows"


class DialogLinux:
    name_class = "DialogLinux"


class Dialog:

    def __new__(cls, *args, **kwargs):
        if TYPE_OS == 1:
            instance = super().__new__(DialogWindows)
        else:
            instance = super().__new__(DialogLinux)
        instance.name = args[0]
    
        return instance