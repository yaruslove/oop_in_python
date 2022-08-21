mtx=[1, 2, 3, 4], [5, 6, 7, 8], [9, 8, 7, 2], [5, 4, 3, 2]

class Check_mtx:
    def __init__ (self):
        pass

    @staticmethod
    def chk_mtrx(mtx):
        pred=len(mtx[0])
        for y in mtx:
            if  not pred==len(y)==len(mtx):
                raise ValueError("Неверный формат для первого параметра matrix.")
            for x in y:
                if not type(x) in (float,int):
                    raise ValueError("Неверный формат для первого параметра matrix.")

a=Check_mtx()

a.chk_mtrx(mtx)
