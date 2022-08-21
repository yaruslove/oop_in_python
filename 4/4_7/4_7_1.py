class Person:
    __slots__ = ('_fio', '_old', '_job')

    def __init__ (self,fio, old, job):
        self._fio, self._old, self._job = fio, old, job

persons = [Person('Суворов', 52, 'полководец'),
        Person('Рахманинов', 50, 'пианист, композитор'),
        Person('Балакирев', 34, 'программист и преподаватель'),
        Person('Пушкин', 32, 'поэт и писатель')
        ]