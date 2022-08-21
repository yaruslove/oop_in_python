class ImageFileAcceptor:
    def __init__ (self,extensions):
        self.extensions=extensions
        
    def __call__ (self, value):
        if value[value.find(".")+1:] in self.extensions:
            return True
        else:
            False