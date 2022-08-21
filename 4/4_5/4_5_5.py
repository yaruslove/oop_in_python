from abc import ABC, abstractmethod

class StackInterface(ABC):
    @abstractmethod
    def push_back(self, obj):
        '''psh_bck'''

    @abstractmethod
    def pop_back(self):
        '''pop_bck'''


class Stack(StackInterface):
    def __init__ (self):
        self._top=None # Первый
        self._last=None # Последний
            
    def push_back(self, obj):
        if self._top == None:
            self._top=obj
            self._last=obj
        else:
            obj._prev=self._last
            self._last._next=obj
            self._last=obj
            
    def pop_back(self):
        if self._last == None:
            return None
        elif self._top==self._last:
            for_return=self._last
            self._top=None # Первый
            self._last=None # Последний
            return for_return
        else:
            for_return=self._last
            self._last=self._last._prev
            self._last._next=None
            return for_return

class StackObj:
    def __init__ (self,data):
        self._data=data
        self._next=None
        self._prev=None


st = Stack()
obj1 = StackObj("obj 1")
st.push_back(obj1)

obj2 = StackObj("obj 2")
st.push_back(obj2)

# obj2 = StackObj("obj 3")
# st.push_back(obj2)

print(st._last._data)

del_obj = st.pop_back()
print(del_obj)
print(st._last._data)
del_obj = st.pop_back()