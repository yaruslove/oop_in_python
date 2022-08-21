class Server:
    prevn=0
    def __new__(cls, *args, **kwargs):
        cls.prevn+=1
        return super().__new__(cls)
        
    def __init__(self):
        self.ip=int(Server.prevn)
        self.buffer=list()
        
    def send_data(self,data):
        Router.buffer.append(data)
    def get_data(self):
        tmp=self.buffer
        self.buffer=list()
        return tmp
        
    def get_ip(self):
        return int(self.ip)

    
    
class Router:
    buffer=list()
    serv_dict=dict()

    @classmethod
    def link(cls,server):
        Router.serv_dict[int(server.get_ip())]=server
    @classmethod
    def unlink(cls,server):
        
        del Router.serv_dict[int(server.get_ip())]
    @classmethod
    def send_data(cls):
        tmp=Router.buffer
        Router.buffer=list()
        for i in tmp:
            Router.serv_dict[i.ip].buffer.append(i)
        
        
    
    
    
class Data:
    def __init__(self,data,ip):
        self.data=data
        self.ip=ip