class ObjList:
    def __init__ (self,data):
        self.__data=""
        self.data=data
        self.__prev=self.__next=None

    @property
    def data(self):
        return self.__data
    
    @data.setter
    def data(self,value):
        if type(value)==str:
            self.__data=value
    
    @property
    def prev(self):
        return self.__prev
    @prev.setter
    def prev(self,obj):
        if type(obj) in (ObjList, type(None)):
            self.__prev=obj   

    @property
    def next(self):
        return self.__next
    @next.setter
    def next(self,obj):
        if type(obj) in (ObjList, type(None)):
            self.__next=obj 
                      

class LinkedList:
    def __init__(self):
        self.head=None  # first object
        self.tail=None  # last object
        
    def add_obj (self,obj):
        obj.prev = self.tail
        if self.tail:
            self.tail.next=obj
        self.tail=obj
        
        if not self.head:
            self.head=obj
    
    def __get_obj_indx(self,indx):
        obj= self.head
        n=0
        while obj and n<indx:
            obj=obj.next
            n+=1
        return obj
    
    def remove_obj(self,indx):
        obj = self.__get_obj_indx(indx)
        if obj is None:
            return
        
        p,n=obj.prev,obj.next
        if p:
            p.next=n
        if n:
            n.prev=p
            
        if self.head== obj:
            self.head= n
        if self.tail == obj:
            self.tail =p
        
    def __len__ (self):
        n=0
        obj=self.head
        while obj:
            obj=obj.next
            n+=1
        return n
    def __call__ (self,index):
        obj = self.__get_obj_indx(index)
        return obj.data if obj else None