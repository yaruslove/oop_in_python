class TriangleListIterator:
    def __init__ (self,spis):
        self.__spis=spis

    def __iter__ (self):
        for i in range (len(self.__spis)):
            for j in range(i+1):
                yield self.__spis[i][j]


a= [["00","01","02","03","04"],
    ["10","11","12","13","14"],
    ["20","21","22","23","24"],
    ["30","31","32","33","34"]]

it = TriangleListIterator(a)

for x in it:  # последовательный перебор всех элементов списка: x00, x10, x11, x20, ...
    print(x)


it_iter = iter(it)
x = next(it_iter)