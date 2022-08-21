class Track:
    def __init__ (self,start_x, start_y):
        self.__track_lst=[]
        self.length=0
        
        if all([type(i) in (int,float) for i in [start_x,start_y]]):
            self.start_x=start_x
            self.start_y=start_y 
            self.__last_point=[self.start_x,self.start_y]     
        else:
            pass

    def add_track(self, tr):
        self.__track_lst.append(tr)
        self.length+=((tr.to_x-self.__last_point[0])**2+(tr.to_y-self.__last_point[1])**2)**0.5
        self.__last_point=[tr.to_x,tr.to_y]

    def get_tracks(self):
        return tuple(self.__track_lst)

    def __eq__ (self,cmp):
        if not isinstance(cmp,Track):
            raise ValueError('Comparable value should be TrackLine obj')
        return self.length==cmp.length

    def  __lt__ (self,cmp):
        if not isinstance(cmp,Track):
            raise ValueError('Comparable value should be TrackLine obj')
        return self.length<cmp.length

    def __len__ (self):
        return int(self.length)

class TrackLine:
    def __init__ (self, to_x, to_y, max_speed):
        if all([type(i) in (int,float) for i in [to_x, to_y, max_speed]]):
            self.to_x, self.to_y, self.max_speed=to_x, to_y, max_speed
        else:
            pass


track1 = Track(0, 0)
track1.add_track(TrackLine(2, 4, 100))
track1.add_track(TrackLine(5, -4, 100))

track2 = Track(0, 1)
track2.add_track(TrackLine(3, 2, 90))
track2.add_track(TrackLine(10, 8, 90))

print(track1.length)
print("track1 == track2 ",track1 == track2 )
print("track1 != track2 ",track1 != track2 )
print("track1 > track2 ",track1 > track2 )
print("track1 < track2 ",track1 < track2 )

