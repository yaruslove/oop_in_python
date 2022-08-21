class Morph:
    def __init__(self,*argums) -> None:
        self.sps=[i.lower() for i in argums]

    def add_word(self, word):
        if not word.lower() in self.sps:
            self.sps.append(word.lower())

    def get_words(self):
        return tuple(self.sps)

    
    def __eq__ (self,v):
        if v.lower() in self.sps:
            return True
        else:
            return False



dict_words = [Morph('связь', 'связи', 'связью', 'связи', 'связей', 'связям', 'связями', 'связях'),
                  Morph('формула', 'формулы', 'формуле', 'формулу', 'формулой', 'формул', 'формулам', 'формулами',
                        'формулах'),
                  Morph('вектор', 'вектора', 'вектору', 'вектором', 'векторе', 'векторы', 'векторов', 'векторам',
                        'векторами', 'векторах'
                        ),
                  Morph('эффект', 'эффекта', 'эффекту', 'эффектом', 'эффекте', 'эффекты', 'эффектов', 'эффектам',
                        'эффектами', 'эффектах'
                        ), Morph('день', 'дня', 'дню', 'днем', 'дне', 'дни', 'дням', 'днями', 'днях'
                                 )]


# text = input()
text="Мы будем устанавливать связь завтра днем."

lst_text=[]
tmp_word=str()
for idx, i in enumerate(text):
    if i.isalpha():
        tmp_word+=i
    else:
        if tmp_word!='':
            lst_text.append(tmp_word)
        tmp_word=str()
    if i.isalpha() and len(text)-1==idx and tmp_word!='':
        lst_text.append(tmp_word)

sht=0
for i in lst_text:
    for j in dict_words:
        if i==j:
            sht+=1
print(sht)