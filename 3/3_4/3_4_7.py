class MaxPooling:
    def __init__(self,step=(2, 2), size=(2,2))->None:
        self.step=step
        self.size=size

    @staticmethod
    def chk_mtrx(mtx):
        pred=len(mtx[0])
        for y in mtx:
            if  not pred==len(y)==len(mtx):
                raise ValueError("Неверный формат для первого параметра matrix.")
            for x in y:
                if not type(x) in (float,int):
                    raise ValueError("Неверный формат для первого параметра matrix.")

    def __call__ (self, a):
        self.chk_mtrx(a)
        step=self.step
        size=self.size

        a_x=[]
        for v in range(len(a)):
            r_p=size[0]
            r_z=0
            a_xtmp=[]
            for idx, i in enumerate(range((len(a[v])-size[0]) //step[0]+1)):
                if i !=0:
                    r_p+=step[0]
                    r_z+=step[0]
                a_xtmp.append(max(a[v][r_z:r_p]))
            a_x.append(a_xtmp)

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
        return a_y

mp = MaxPooling(step=(2, 2), size=(2,2))
res = mp([[1, 2, 3, 4], [5, 6, 7, 8], [9, 8, 7, 6], [5, 4, 3, 2]])
