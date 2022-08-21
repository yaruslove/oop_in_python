class VideoItem:
    def __init__ (self,title, descr, path):
        self.title, self.descr, self.path=title, descr, path
        self.rating=VideoRating()

class VideoRating:
    def __init__ (self):
        self.__rating=0

    @property
    def rating(self):
        return self.__rating

    @rating.setter
    def rating(self,v):
        if v in [0,1,2,3,4,5]:
            self.__rating=v
        else:
            raise ValueError('неверное присваиваемое значение')


        