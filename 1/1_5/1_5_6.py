class CPU:
    def __init__ (self,name,fr):
        self.name=name
        self.fr=fr


class Memory:
    def __init__(self,name,volume):
        self.name=name
        self.volume=volume


class MotherBoard:
    def __init__(self,name,cpu,*mem):
        self.name=name
        self.cpu=cpu
        self.total_mem_slots=4
        self.mem_slots=list(mem)[:self.total_mem_slots]
    def get_config(self):
        return ["Материнская плата: {}".format(self.name), \
                "Центральный процессор: {}, {}".format(self.cpu.name,self.cpu.fr), \
                "Слотов памяти: {}".format(self.total_mem_slots),
                "Память: {}".format("; ".join(["{} - {}".format(i.name,i.volume) for i in self.mem_slots]))]

mb=MotherBoard("Gigabyte",CPU("intel",2000), Memory('hyper',4),Memory('hunix',8),Memory('kingston',12))


