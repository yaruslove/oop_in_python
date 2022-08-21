class Point:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    # def __getattr__(self, item):
    #     return object.__getattribute__(self, item)

pt = Point(1, 2)

try:
    pt.z
except:
    print("Атрибут с именем z не существует")
