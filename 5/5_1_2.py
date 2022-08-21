# lst_in = "1 -5.6 2 abc 0 False 22.5 hello world"
lst_in= "8 11 abcd -7.5 2.0 -5" #  Answer 14

print(lst_in.split() )

lst_in=lst_in.split()

def chk(x):
    if x[0]=='-':
        x=x[1:]
    if x.isdigit():
        return True

lst_in=list(map(int, list(filter(chk, lst_in))))
print(sum(lst_in))