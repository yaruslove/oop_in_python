class Translator:
    __slovar=dict()
    def add(self,eng,rus):
        if eng in self.__slovar.keys() and rus not in self.__slovar[eng]:
            self.__slovar[eng].append(rus)
        elif eng not in self.__slovar.keys():
            self.__slovar[eng]=[rus]
        else:
            pass
    
    def remove(self, eng):
        if eng in self.__slovar.keys():
            self.__slovar.pop(eng)
    def translate(self,eng):
        return self.__slovar[eng]
    
tr=Translator()


tmp=[['tree', 'дерево'],
 ['car', 'машина'],
 ['car', 'автомобиль'],
 ['leaf', 'лист'],
 ['river', 'река'],
 ['go', 'идти'],
 ['go', 'ехать'],
 ['go', 'ходить'],
 ['milk', 'молоко']]

for i in tmp:
    tr.add(i[0],i[1])
    
tr.remove("car")

print(' '.join(tr.translate("go")))