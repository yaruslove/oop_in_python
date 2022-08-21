a=[1, 2,  3, 4,5,6,7,8,9,10,11,12,13,14,15,16]


size=(3,3)
step=(2,2)

r_p=size
r_z=0
for i in range((len(a)-size) //step+1):
    if i !=0:
        r_p+=step
        r_z+=step
    print(a[r_z:r_p])





# ### 1
# it=0
# size=3
# step=1

# r_p=size
# r_z=0
# # print(a[r_z:r_p])

# ### 2
# it=1
# size=3
# step=2

# r_p=r_p+step
# r_z=r_z+step
# # print(a[r_z:r_p])

# # print((len(a)-size) //step)




