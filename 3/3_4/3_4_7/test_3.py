a=[[1, 2,  3, 4, 5, 6, 7, 8, 9,10,11,12,13,14,15],
   [16,17,18,19,20,21,22,23,24,25,26,27,28,29,30],
   [31,32,33,34,35,36,37,38,39,40,41,42,43,44,45],
   [46,47,48,49,50,51,52,53,54,55,56,57,58,59,60],
   [61,62,63,64,65,66,67,68,69,70,71,72,73,74,75]]


size=(3,2)
step=(3,2)


v=0 # значение по вертикали

a_x=[]

for v in range(len(a)):
   r_p=size[0]
   r_z=0
   
   a_xtmp=[]
   for idx, i in enumerate(range((len(a[v])-size[0]) //step[0]+1)):
      if i !=0:
         r_p+=step[0]
         r_z+=step[0]
         
      print(a[v][r_z:r_p])
      a_xtmp.append(max(a[v][r_z:r_p]))
   a_x.append(a_xtmp)
print(a_x)