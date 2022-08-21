class Vector:
    def __init__(self, *args) -> None:
        self.arg = list(args)

    def __len__(self):
        return len(self.arg)

    def __add__(self, o):
        if len(self) != len(o):
            raise ArithmeticError('размерности векторов не совпадают')
        return Vector(*[a+b for a, b in zip(self.arg, o.arg)])

    def __iadd__(self, o):
        if isinstance(o, int):
            self.arg = list(map(lambda x: x + o, self.arg))
        else:
            if len(self) != len(o):
                raise ArithmeticError('размерности векторов не совпадают')
            else:
                self.arg = [a+b for a, b in zip(self.arg, o.arg)]
        return self
    
    def __sub__(self, o):
        if len(self) != len(o):
            raise ArithmeticError('размерности векторов не совпадают')
        return Vector(*[a-b for a, b in zip(self.arg, o.arg)])

    def __isub__(self, o):
        if isinstance(o, int):
            self.arg = list(map(lambda x: x - o, self.arg))
        else:
            if len(self) != len(o):
                raise ArithmeticError('размерности векторов не совпадают')
            else:
                self.arg = [a-b for a, b in zip(self.arg, o.arg)]
        return self
    
    def __mul__(self, o):
        if len(self) != len(o):
            raise ArithmeticError('размерности векторов не совпадают')
        return Vector(*[a*b for a, b in zip(self.arg, o.arg)])

    def __eq__(self, o):
        if len(self) != len(o):
            raise ArithmeticError('размерности векторов не совпадают')
        return all([a == b for a ,b in zip(self.arg, o.arg)])
