# здесь объявляйте декоратор и все что с ним связано
def class_log(log_lst):
    def wrapper_log_method(cls):
        methods = {k: v for k, v in cls.__dict__.items() if callable(v)}
        for k, v in methods.items():
            setattr(cls, k, decorator(v))
        return cls
        
    def decorator(func):
        def wrapper (*argums, **kargums):
            log_lst.append(func.__name__)
            return func(*argums, **kargums)
        return wrapper

    return wrapper_log_method

vector_log = []   # наименование (vector_log) в программе не менять!


@class_log(vector_log)
class Vector:
    def __init__(self, *args):
        self.__coords = list(args)

    def __getitem__(self, item):
        return self.__coords[item]

    def __setitem__(self, key, value):
        self.__coords[key] = value