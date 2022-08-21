class IteratorAttrs:
    def __init__ (self):
        pass
    def __iter__(self):
        for key, value in self.__dict__.items():
            yield (key, value)



class SmartPhone(IteratorAttrs):
    def __init__ (self,model, size, memory):
        self.model, self.size, self.memory= model, size, memory


#Test_1
itr=IteratorAttrs()

for i in itr:
    print(i)


#Test_2
phone = SmartPhone("samsung s22", (67, 147), 8)

for attr, value in phone:
    print(attr, value)