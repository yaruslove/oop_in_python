import sys

# здесь пишите программу
class Book:
    def __init__ (self,title, author, pages):
        self.title=title
        self.author=author
        self.pages=pages
    
    def __str__(self):
        return f"Книга: {self.title}; {self.author}; {str(self.pages)}"

lst_in = list(map(str.strip, sys.stdin.readlines())) # считывание списка из входного потока (эту строчку не менять)

book = Book(lst_in[0], lst_in[1], lst_in[2])
print(book)