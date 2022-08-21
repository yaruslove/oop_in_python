a= "01: 02: 03"
hr_list=[int(i) for i in a.split(":")]

cort=[3600,60,1]
vr=0
for i,j in zip(hr_list,cort):
    vr+=i*j
print(vr)