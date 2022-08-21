class NewList:
    def __init__(self,l=list()):
        self.l=l

    @staticmethod
    def raznica(l,sub):
        for i in sub:
            idx_del = [ d for d in range(len(l)) if l[d] is i ]
            if not idx_del==[]:
                del l[idx_del[0]]
        return l


    def __sub__ (self,other):
        l=self.l[:]
        sub=other
        if not isinstance(other, (list,NewList)):
            raise ArithmeticError
        if isinstance(other,NewList):
            sub=other.l
        l=self.raznica(l,sub)
        
        return NewList(l)

    def __rsub__ (self, other):
        l=self.l[:]
        sub=other
        if not isinstance(other, (list,NewList)):
            raise ArithmeticError
        if isinstance(other,NewList):
            sub=other.l

        l=self.raznica(sub,l)
        
        return NewList(l)



    def get_list(self):
        return  self.l



# lst1 = NewList([11,0,0,1,1, 2, -4,5.0,-7.87, 6, 10, 11, 15, False, True])
# lst2 = NewList([0, 2, 3, True,11,True, True])
# res1 = lst1-lst2 # NewList: [-4, 6, 10, 11, 15, False]
# print("res1",res1.get_list())


# lst1 = NewList([11,0,0,1,1, 2, -4,5.0,-7.87, 6, 10, 11, 15, False, True])
# # lst2 = NewList([0, 2, 3, True,11,True, True])
# res1=[0, 2, 3,4, True,11,True, True,False]-lst1 # NewList: [-4, 6, 10, 11, 15, False]
# print("res1",res1.get_list())


lst1 = NewList([1, 2, -4, 6, 10, 11, 15, False, True])
lst2 = NewList([0, 1, 2, 3, True,])
res_1 = lst1 - lst2 # NewList: [-4, 6, 10, 11, 15, False]
print("\n")
print("res_1",res_1.get_list())

lst1 -= lst2 # NewList: [-4, 6, 10, 11, 15, False]
print("lst1",lst1.get_list())
res_2 = lst2 - [0, True] # NewList: [1, 2, 3]
print("res_2",res_2.get_list())

res_3 = [1, 2, 3, 4.5] - res_2 # NewList: [4.5]
print("res_3",res_3.get_list())

a = NewList([2, 3])
res_4 = [1, 2, 2, 3] - a # NewList: [1, 2]
print("res_4",res_4.get_list())
