stich = ["Я к вам пишу – чего же боле?",
        "Что я могу еще сказать?",
        "Теперь, я знаю, в вашей воле",
        "Меня презреньем наказать.",
        "Но вы, к моей несчастной доле",
        "Хоть каплю жалости храня,",
        "Вы не оставите меня."]

class StringText:
    def __init__ (self,stroch):
        self.stroch=stroch


    def __lt__ (self,v):
        return len(self.stroch)<len(v.stroch)
    
    def __le__ (self,v):
        return len(self.stroch)<=len(v.stroch)

    def __repr__ (self):
        return f'StringText({str(self.stroch)})'



lst_text=[]
for i in stich:
    for t in list("–?!,.;"):
        i=i.replace(t, '').strip()
    s=i.split(" ")
    s=[j for j in s if j!=""]
    lst_text.append(StringText(s))

lst_text_sorted = sorted(lst_text, key= lambda x: len(x.stroch),reverse=True)

def turn_to_str(s):
    r=str()
    for i in s:
        r+=f'{i} '
    return r.strip()

lst_text_sorted=[turn_to_str(i.stroch) for i in lst_text_sorted]
print("lst_text_sorted", lst_text_sorted)
