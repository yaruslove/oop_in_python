# lst_in = "1 -5.6 True abc 0 23.56 hello"
lst_in = 'hello 1 world -2 4.5 True'

print(lst_in.split())

lst_in=lst_in.split()

lst_out=[]
for i in lst_in:
    if i[0]=='-' and i[1:].isdigit():
        lst_out.append(int(i))
    elif i.isdigit():
        lst_out.append(int(i))
    else:
        try:
            lst_out.append(float(i))
            continue
        except ValueError:
            lst_out.append(i)


print(lst_out)
