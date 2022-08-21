class StackObj:
    def __init__ (self,data):
        self.data:str = data
        self.next:StackObj = None
        self.prev:StackObj = None

class Stack:
    def __init__ (self):
        self.top = None
        self.first = None
    def push_back(self, obj):
        if self.top==None:
            self.top=obj
            self.first=obj
        else:
            obj.prev=self.top
            self.top.next=obj
            self.top=obj

    def push_front(self, obj):
        if self.top==None:
            self.top=obj
            self.first=obj
        else:
            obj.next= self.first
            self.first.prev=obj
            self.first=obj


    def __getitem__ (self,indx):
        if not(type(indx)==int and indx>=0):
            raise IndexError('неверный индекс')
        if self.first==None:
            return None
        else:
            cur_index=0
            cur_obj=self.first
            while True: # cur_obj.next!=None
                if cur_index==indx:
                    return cur_obj.data
                cur_obj=cur_obj.next
                cur_index+=1
                if cur_obj==None:
                    raise IndexError('неверный индекс')

    def __setitem__ (self,indx,value):
        if not(type(indx)==int and indx>=0):
            raise IndexError('неверный индекс')
        if self.first==None:
            return None
        else:
            cur_index=0
            cur_obj=self.first
            while True: # cur_obj.next!=None
                if cur_index==indx:
                    cur_obj.data=value
                    break
                cur_obj=cur_obj.next
                cur_index+=1
                if cur_obj==None:
                    raise IndexError('неверный индекс')

    def pop(self):
        if self.top==None:
            return None
        elif self.top==self.first:
            rtrn=self.top
            self.top=self.first=None
            return rtrn
        else:
            rtrn=self.top
            self.top=self.top.prev
            return rtrn

    def __repr__(self):
        rtrn=str()
        cur_obj=self.first
        if self.first==None:
            return "empty"
        else:
            while True:
                rtrn+=f"{cur_obj.data}, "
                if cur_obj.next==None:
                    return rtrn.strip()
                cur_obj=cur_obj.next

    def __iter__(self):
        self.obj=self.first
        self.rtrn=self.first
        return self

    def __next__ (self):
        if self.rtrn.next==None:
            raise StopIteration
        self.rtrn=self.obj
        self.obj=self.obj.next
        return self.rtrn


o1=StackObj("o1")
o2=StackObj("o2")
o3=StackObj("o3")
o4=StackObj("o4")


st = Stack()


st.push_back(o2)
st.push_back(o3)
st.push_back(o4)
st.push_front(o1)

print(st)

for obj in st: # перебор объектов стека (с начала и до конца)
    print(obj.data)  # отображение данных в консоль

print("HERE")
for obj in st: # перебор объектов стека (с начала и до конца)
    print(obj.data)  # отображение данных в консоль

print(st[1])



