class Validator:
    def _is_valid(self, data):
        raise NotImplementedError('в классе не переопределен метод _is_valid')

class FloatValidator(Validator):
    def __init__ (self,min_value, max_value):
        self.min_value, self.max_value=min_value,max_value

    def __call__(self, v):
        if type(v) == float and self.min_value <= v and v <= self.max_value:
            return True
        else:
            return False