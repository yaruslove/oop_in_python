# %%
class DeltaClock:
    def __init__(self,clock1, clock2) -> None:
        self.clock1=clock1
        self.clock2=clock2

    def __diff_time(self):
        # Sec
        if self.clock1.seconds>=self.clock2.seconds:
            diff_s=self.clock1.seconds-self.clock2.seconds
            tmp_clock1_min=self.clock1.minutes
        else:
            tmp_clock1_min=self.clock1.minutes-1
            diff_s=self.clock1.seconds+60-self.clock2.seconds

        # Min
        if tmp_clock1_min>=self.clock2.minutes:
            diff_m=tmp_clock1_min-self.clock2.minutes
            tmp_clock1_hr=self.clock1.hours
        else:
            tmp_clock1_hr=self.clock1.hours-1
            diff_m=tmp_clock1_min+60-self.clock2.minutes

        # Hr
        if tmp_clock1_hr>=self.clock2.hours:
            diff_h=tmp_clock1_hr-self.clock2.hours
        else:
            return "00: 00: 00"

        return f"{str(diff_h).zfill(2)}: {str(diff_m).zfill(2)}: {str(diff_s).zfill(2)}"


    def __str__ (self):
        return self.__diff_time()

    def __len__ (self):
        str_dif=self.__diff_time()
        hr_list=[int(i) for i in str_dif.split(":")]

        cort=[3600,60,1]
        vr=0
        for i,j in zip(hr_list,cort):
            vr+=i*j

        return vr
# %%
class Clock:
    def __init__(self,hours, minutes, seconds):
        self.hours=hours
        self.minutes=minutes
        self.seconds=seconds

    def get_time(self):
         return self.hours * 3600 + self.minutes * 60 + self.seconds
# %%
dt = DeltaClock(Clock(2, 45, 0), Clock(1, 15, 0))
print(dt) # 01: 30: 00
len_dt = len(dt) # 5400

print(len_dt)