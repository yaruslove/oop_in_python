class StackObj:
    def __init__ (self,data):
        self.data:str = data
        self.next:StackObj = None
        self.prev:StackObj = None

class Stack:
    def __init__ (self):
        self.top = None
        self.first = None
    def push(self, obj):
        if self.top==None:
            self.top=obj
            self.first=obj
        else:
            obj.prev=self.top
            self.top.next=obj
            self.top=obj

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
                    return cur_obj
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
                    tmp_obj_prev=cur_obj.prev
                    tmp_obj_next=cur_obj.next
                    tmp_obj_prev.next=value
                    tmp_obj_next.prev=value
                    value.next=tmp_obj_next
                    value.prev=tmp_obj_prev
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