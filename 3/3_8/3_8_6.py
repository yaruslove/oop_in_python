class RadiusVector:
    def __init__ (self, *argums):
        self.coords=list(argums)

    def __getitem__ (self,indx):
        if type(indx) == slice:
            return tuple(self.coords[indx])
        else:
            return self.coords[indx]

    def __setitem__ (self,indx,value):
        self.coords[indx]=value