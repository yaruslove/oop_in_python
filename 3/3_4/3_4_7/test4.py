
# size=(3,2)
# step=(3,1)

# a_x=[[3,  6,  9, 12, 15], 
#     [18, 21, 24, 27, 30], 
#     [33, 36, 39, 42, 45],
#     [48, 51, 54, 57, 60]]


size=(3,2)
step=(3,1)

a_x=[[3,  6,  9, 12, 15],
    [18, 21, 24, 27, 30], 
    [33, 36, 39, 42, 45], 
    [48, 51, 54, 57, 60],] #     [63, 66, 69, 72, 75]


a_y=[]
r_z=0
r_p=size[1]
for k in range((len(a_x)-size[1])//step[1]+1):
    if k !=0:
        r_z+=step[1]
        r_p+=step[1]
    y_tmp1=[]
    for j in range(len(a_x[0])):
        y_tmp2=[]
        for i in range(r_z,r_p):
            y_tmp2.append(a_x[i][j])
        y_tmp1.append(max(y_tmp2))
    a_y.append(y_tmp1)
print(a_y)
