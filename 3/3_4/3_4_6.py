class Box3D:
    def __init__ (self,width, height, depth):
        self.width=width
        self.height=height
        self.depth=depth
    def __add__ (self,v):
        r=Box3D(0,0,0)
        r.width=v.width+self.width
        r.height=v.height+self.height
        r.depth=v.depth+self.depth
        return r

    def __mul__ (self,v):
        r=Box3D(0,0,0)
        r.width=v*self.width
        r.height=v*self.height
        r.depth=v*self.depth
        return r

    def __rmul__ (self,v):
        return self*v

    def __sub__ (self,v):
        r=Box3D(0,0,0)
        r.width=self.width-v.width
        r.height=self.height-v.height
        r.depth=self.depth-v.depth
        return r


    def __floordiv__ (self,v):
        r=Box3D(0,0,0)
        r.width=self.width//v
        r.height=self.height//v
        r.depth=self.depth//v
        return r

    def __mod__ (self,v):
        r=Box3D(0,0,0)
        r.width=self.width%v
        r.height=self.height%v
        r.depth=self.depth%v
        return r

box1 = Box3D(1, 2, 3)
box2 = Box3D(2, 4, 6)

box = box1 + box2
print(box.width,box.height,box.depth)

box = box1 *2
print(box.width,box.height,box.depth)

box = 3 * box2
print(box.width,box.height,box.depth)

box = box2 - box1
print(box.width,box.height,box.depth)

box = box1 // 2
print(box.width,box.height,box.depth)

box = box2 % 3 
print(box.width,box.height,box.depth)

