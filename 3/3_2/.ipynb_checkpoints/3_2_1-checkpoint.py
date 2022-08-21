from random import randint,choice
# import random


class RandomPassword:
    def __init__ (self,psw_chars, min_length, max_length):
        self.psw_chars=psw_chars
        self.min_length=min_length
        self.max_length=max_length
        
    def __call__ (self, *args, **kwargs):
        self.__psw=str()
        list_chars=list(self.psw_chars)
        for i in range(randint(self.min_length, self.max_length)):
            self.__psw+=choice(list_chars)
        return self.__psw

min_length = 5
max_length = 20
psw_chars = "qwertyuiopasdfghjklzxcvbnm0123456789!@#$%&*"

rnd = RandomPassword(psw_chars, min_length, max_length)

lst_pass=[rnd() for i in range(3)]
lst_pass