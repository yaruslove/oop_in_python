class Person:
    def __init__ (self,fio, job, old, salary, year_job):
        self.fio=fio
        self.job=job
        self.old=old
        self.salary=salary
        self.year_job=year_job
        self.lst=[self.fio, self.job, self.old, self.salary, self.year_job]

        self.start = 0
        self.stop = 4
        self.step = 1
        self.value = self.start - self.step

    def __check (self,k):
        if type(k)!=int and not (0<=len(self.lst)<=4):
            raise IndexError('неверный индекс')
    def __getitem__ (self,k):
        self.__check(k)
        return self.lst[k]
    def __setitem__ (self,k,v):
        self.__check(k)
        self.lst[k]=v

    def __next__ (self):
        if self.value + self.step < self.stop:
            self.value += self.step
            return self.lst[self.value]
        else:
            raise StopIteration

    def __iter__ (self):
        self.value = self.start-self.step
        return self


pers = Person('Гейтс Б.', 'бизнесмен', 61, 1000000, 46)
pers[0] = 'Балакирев С.М.'
for v in pers:
    print(v)

