class LengthValidator:
    def __init__ (self, min_length, max_length):
        self.min_length=min_length
        self.max_length=max_length
        
    def __call__ (self, value):
        return self.min_length <= len(value)<= self.max_length
    

class CharsValidator:
    def __init__ (self,chars):
        self.chars=chars
    
    def __call__ (self, value):
        return all([i in list(self.chars) for i in list(value)])