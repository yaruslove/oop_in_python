class Rect:
    def __init__ (self, x, y, width, height):
        self.x=x
        self.y=y
        self.width=width
        self.height=height

    def __hash__ (self):
        return (hash((self.width, self.height)))

c=Rect(1,2,3,4)
print(hash(c))
