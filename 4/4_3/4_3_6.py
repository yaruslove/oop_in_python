class SoftList(list):
    def __getitem__(self,k):
        if k>=0 and k>=len(self):
            return False
        if k<0 and abs(k)-1>=len(self):
            return False
        return super().__getitem__(k)

sl = SoftList("python")
print(sl[0]) # 'p'
print(sl[-1]) # 'n'
print(sl[6]) # False
print(sl[-7]) # False