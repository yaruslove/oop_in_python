from string import ascii_lowercase, digits
import string 


# здесь объявляйте классы TextInput и PasswordInput

class TextInput:
    CHARS="абвгдеёжзийклмнопрстуфхцчшщьыъэюя "+string.ascii_lowercase+"1234567890"
    CHARS_CORRECT=CHARS+CHARS.upper()
    new_set=set(list(CHARS_CORRECT))
    def __init__ (self,name,size=10):
        self.check_name(name)
        self.name=name
        self.size=size
    def get_html(self):
        return f"<p class='login'>{self.name}: <input type='text' size={self.size} />"
    
    @classmethod
    def check_name(cls, name):
        lengh= 3<=len(name)<=50
        crct=all([i in cls.new_set for i in name])
        if lengh and crct:
            return True
        else:
            raise ValueError('некорректное имя поля')

            
class PasswordInput:
    CHARS="абвгдеёжзийклмнопрстуфхцчшщьыъэюя "+string.ascii_lowercase+"1234567890"
    CHARS_CORRECT=CHARS+CHARS.upper()
    new_set=set(list(CHARS_CORRECT))
    def __init__ (self,name,size=10):
        self.check_name(name)
        self.name=name
        self.size=size
    def get_html(self):
        return f"<p class='password'>{self.name}: <input type='text' size={self.size} />"
    
    @classmethod
    def check_name(cls, name):
        lengh= 3<=len(name)<=50
        crct=all([i in cls.new_set for i in name])
        if lengh and crct:
            return True
        else:
            raise ValueError('некорректное имя поля')            

class FormLogin:
    def __init__(self, lgn, psw):
        self.login = lgn
        self.password = psw

    def render_template(self):
        return "\n".join(['<form action="#">', self.login.get_html(), self.password.get_html(), '</form>'])


# эти строчки не менять
login = FormLogin(TextInput("Логин"), PasswordInput("Пароль"))
html = login.render_template()