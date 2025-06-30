# isme 2 class bnani hen 2 d vectr and 3dvector or 3d waly me 2d ka data use krna hy 

class twod():
    def __init__(self , i , j):
        self.i = i
        self.j = j
    def show(self):
        print(f"the vector i {self.i} + {self.j}j")
        
class threed(twod):
    def __init__(self, i, j , k):
        super().__init__(i, j)
        self.k = k
        
    def show(self):
        print(f"the vector i {self.i} + {self.j}j + {self.k}k")
        
a = twod( 1 ,2 )
b = threed(1 , 2 ,3)
a.show()
b.show()