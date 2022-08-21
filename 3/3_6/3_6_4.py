class BookStudy:
    def __init__ (self,name, author, year):
        self.name: str =name
        self.author: str=author
        self.year:str =year
    def __hash__ (self):
        return hash((self.name.lower(),self.author.lower()))
    def __eq__ (self,v):
        return hash((self.name.lower(),self.author.lower()))==hash((v.name.lower(),v.author.lower()))

lst_in = [
    'Python; Балакирев С.М.; 2020',
    'Python ООП; Балакирев С.М.; 2021',
    'Python ООП; Балакирев С.М.; 2022',
    'Python; Балакирев С.М.; 2021',
]

lst_bs=list()
for i in lst_in:
    name, author, year=i.split("; ")
    lst_bs.append(BookStudy(name, author, year))

unique_books=len(set(lst_bs))