from math import sqrt

class RadiusVector:
    def __init__ (self, *args):
        self.__vector=list()
        if len(args)==1 and isinstance(args[0],int) and args[0]>1:
            for _ in range(args[0]):
                self.__vector.append(0)
        else:
            self.__from_list(args)
    
    def __from_list(self,args):
        for i in args:
            self.__vector.append(i)

    def set_coords(self, *args):
        # self.__vector=list()
        ch=len(self.__vector)
        for indx,i in enumerate(args[:ch]):
            self.__vector[indx]=i

    def get_coords(self):
        return tuple([i for i in self.__vector])

    def __len__(self):
        return  len(self.__vector)
    
    def __abs__ (self):
        lenght=0
        for crd in self.__vector:
            lenght+=crd**2
        return sqrt(lenght)



vector3D = RadiusVector(5)

print(vector3D.get_coords())
vector3D.set_coords(3, -5.6, 8)

print(vector3D.get_coords())
