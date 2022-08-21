class Point:

    def __new__(cls, *args, **kwargs):

        print("1. Create a new instance of Point.")

        return super().__new__(cls)


    def __init__(self, x, y):

        print("2. Initialize the new instance of Point.")

        self.x = x

        self.y = y


    def __repr__(self) -> str:

        return f"{type(self).__name__}(x={self.x}, y={self.y})"
