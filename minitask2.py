class Vec():
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y
    def __sub__(self,other):
        return [self.x-other.x,self.y-other.y]
    def __str__(self):
        return 'vector is {},{}'.format(self.x,self.y)

v0=Vec()
v1=Vec(2,3)
v2=Vec(1,4)
res=v2-v1
print(res)
