class Cat(str):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"{self.name}"

cat = Cat('Васька')

a=cat
print(a)