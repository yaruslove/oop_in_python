import sys

# здесь объявляются все необходимые классы

# считывание списка из входного потока (эту строку не менять)
lst_in = list(map(str.strip, sys.stdin.readlines())) # список lst_in в программе не менять

import sys


class ListObject:
    def __init__(self,data):
        self.data=data
        self.next_obj=None
    def link(self, obj):
        self.next_obj=obj

        
head_obj=ListObject(lst_in[0])
obj=head_obj

for i in range(1,len(lst_in)):
    obj_new=ListObject(lst_in[i])
    obj.link(obj_new)
    obj=obj_new