# make clss vector representing a vector of n dimensions . overlaod the + and * operator which calculates sum and dot prduct of them 

class vector:
    def __init__(self_init, x ,y  ,z ):
     self_init.x = x
     self_init.y = y
     self_init.z = z
     
    def __add__(selfadd1, selfadd2):
        result = vector(selfadd1.x + selfadd2.x , selfadd1.y +selfadd2.y , selfadd1.z +selfadd2.z )
        return result
    def __mul__(self , other):
        result = self.x * other.x + self.y * other.y + self.z*other.z
        return result
    
    def __str__(self):
       return f"vector({self.x}i + {self.y}j + {self.z}k)"
   
   
v1 = vector(1 , 2 ,3 )
v2 = vector(4 , 5 , 6)
v3 = vector(7 , 8 ,9)

print(v1 + v2)
print(v1 * v2)
