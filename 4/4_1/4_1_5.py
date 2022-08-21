class Validator:
    def _is_valid(self, data):
        if type(data)==self.data_type and self.min_value<=data<=self.max_value  :
            return True
        else:
            raise ValueError('данные не прошли валидацию')

    def __call__(self,data):
        return self._is_valid(data)



class IntegerValidator(Validator):
    def __init__ (self,min_value, max_value):
        self.min_value=min_value
        self.max_value=max_value
        self.data_type=int

class FloatValidator(Validator):
    def __init__ (self,min_value, max_value):
        self.min_value=min_value
        self.max_value=max_value
        self.data_type=float

integer_validator = IntegerValidator(-10, 10)
float_validator = FloatValidator(-1, 1)
res1 = integer_validator(10)  # True
print(res1)
res2 = float_validator(10)