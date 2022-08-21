class Figure:
    type_fig='ellipse'
    color='red' 
    
fig1=Figure()
fig1.start_pt= (10, 5)
fig1.end_pt=(100, 20)
fig1.color='blue'

del fig1.color

tmp=str()
for i in list(fig1.__dict__.keys()):
    tmp="{} {}".format(tmp,i).strip()
print(tmp)