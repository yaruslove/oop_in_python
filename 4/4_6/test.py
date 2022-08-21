class A:
    def __init__(self, name, old):
        super().__init__()
        self.name = name
        self.old = old


class B:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class C(B, A):
    def __init__(self, name, old, weight, height):
        super().__init__(name, old)
        self.weight = weight
        self.height = height

person = C("Balakirev", 33, 80, 185)
print(person.weight)
print(person.height)
print(person.name)
print(person.old)