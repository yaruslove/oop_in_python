class StackObj:
    def __init__ (self,data):
        self.__data =data
        self.__next=None
        self.prev=None
    
    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self,obj):
        self.__next=obj

    @property
    def data(self):
        return self.__data

    
class Stack:
    def __init__ (self):
        self.top=None
        self.__last=None

    def push_back(self, obj):
        if self.top == None:
            self.top=obj
            self.__last=obj
        else:
            self.__last.next=obj
            obj.prev=self.__last
            self.__last=obj


    def pop_back(self):
        if self.top == self.__last:
            self.top=None
            self.__last=None
        elif self.top!=None:
            self.__last=self.__last.prev

    @property
    def last(self):
        return self.__last
    
    @last.setter
    def last(self,value):
        self.__last=value

    def __add__ (self,another):
        self.push_back(another)
        return self

    def __iadd__ (self,another):
        self.push_back(another)
        return self

    def __mul__ (self,another):
        for i in another:
            self.push_back(StackObj(i))
        return self
    
    def __imul__ (self,another):
        for i in another:
            self.push_back(StackObj(i))
        return self
        

obj1 = StackObj("1")
obj2 = StackObj("2")
obj3 = StackObj("3")

st = Stack()

st.push_back(obj1)

st=st+obj2
print("type",type(st))
print("Last",st.top.data)
print("Last anth way",st.last.data,"\n")




# st.push_back(obj1)
# st.push_back(obj2)
# st.push_back(obj3)

# print("Last",st.top.next.next.data)
# print("Last anth way",st.last.data,"\n")

# st.pop_back()

# print("Last",st.top.next.data)
# print("Last anth way",st.last.data,"\n")

# st.pop_back()

# print("Last",st.top.data)
# print("Last anth way",st.last.data,"\n")

# st.pop_back()

# print("Last",st.top)
# print("Last anth way",st.last,"\n")
