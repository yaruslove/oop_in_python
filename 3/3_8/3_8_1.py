class Record:
    def __init__ (self,**keyargs):
        self.keyargs=keyargs
        self.slov={}
        s=0
        for key, value in self.keyargs.items():
            self.slov[s]=dict()
            self.slov[s][key]=self.key=value
            setattr(self, key, value)
            s+=1
            """
            Обьяснение словаря
            # self.slov={0:{pk:1},1:{title:'Python ООП'},2:{author:'Балакирев'}}
            """

    def __getitem__ (self,v):
        if not(len(self.slov)>v and isinstance(v,int)):
            raise IndexError('неверный индекс поля')
        z=list(self.slov[v].keys())[0]
        return self.slov[v][z]

    def __setitem__ (self,key,value):
        if not(len(self.slov)>key and isinstance(key,int)):
            raise IndexError('неверный индекс поля')
        z=list(self.slov[key].keys())[0]
        setattr(self, z, value)
        self.slov[key][z]=value
        # self.__dict__["keyargs"][z]=value




r = Record(pk=1, title='Python ООП', author='Балакирев')


print(r.pk) # 1
print(r.title) # Python ООП
print(r.author) # Балакирев

print("")
r[0] = 2 # доступ к полю pk
print(r.pk) 
r[1] = 'Супер курс по ООП' # доступ к полю title
print(r.title) 
r[2] = 'Балакирев С.М.' # доступ к полю author
print(r.author) 
print(r[1]) # Супер курс по ООП
# r[3] # генерируется исключение IndexError


# print(r.pk)
# print(r.author)

# print(r[0])
# print(r[1])
# r[1]="Ogon"
# print(r[1])

# print(r.author)

# print(r.__dict__)
# print(r.title)

