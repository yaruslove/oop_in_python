filenames = ["boat.jpg", "web.png", "text.txt", "python.doc", "ava.jpg", "forest.jpeg", "eq_1.png", "eq_2.xls"]

class FileAcceptor:
    def __init__(self, *argums):
        if type(argums[0])==list:
            self.extns= list(set([i for i in argums[0]]))
        else:
            self.extns=list(set(argums))
            # print(self.extns)

    def __call__ (self,v):
        return any([v.endswith(sufix) for sufix in self.extns])


    def __add__ (self, v):
        tmp=self.extns+v.extns
        return FileAcceptor(tmp)

# acceptor1=FileAcceptor("mp3","wav")
# acceptor2=FileAcceptor("avi","flc")

# acceptor12 = acceptor1 + acceptor2

# print(type(acceptor12.extns))
# print(acceptor12.extns)

acceptor1 = FileAcceptor("jpg", "jpeg", "png")
acceptor2 = FileAcceptor("png", "bmp")
acceptor12 = acceptor1 + acceptor2    # ("jpg", "jpeg", "png", "bmp")


acceptor_images = FileAcceptor("jpg", "jpeg", "png")
acceptor_docs = FileAcceptor("txt", "doc", "xls")
filenames = list(filter(acceptor_images + acceptor_docs, filenames))
