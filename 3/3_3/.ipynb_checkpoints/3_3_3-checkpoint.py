class WordString:
    def __init__ (self,contxt=None):
        if contxt!=None:
            self.string=contxt

    # def __setattr__(self,key,value):
    #     if key=="string":
    #         self.__list_of_word(value)
    #     object.__setattr__(self,key,value)
    
    @property
    def string(self):
        return self.__string
    
    @string.setter
    def string(self, string):
        self.__list_of_word(string)
        self.__string = string
                   
    def __list_of_word(self,value):
        self.pure_list=list()
        for i in value.split(" "):
            if i!="":
                self.pure_list.append(i)

    def __len__(self):
        return len(self.pure_list)
    
    def __call__(self, number):
        if isinstance(number, int) and number>=0:
            return self.pure_list[number]
        
words = WordString()
words.string = "Курс по Python ООП"
n = len(words)
first = "" if n == 0 else words(0)
print(words.string)
print(f"Число слов: {n}; первое слово: {first}")