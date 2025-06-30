# super method use krty hen jb hmen ek ek instructor ko call krna 
# ho mtlb ke hm uske prent ke isntructor ko bhi call kren 


class employee():
    a = 1
    def __init__(self):
        print("This is emplyee constructor")
class programmer(employee): # sb employee wala agaya
    b = 2
    def __init__(self):
        print("This is programmer constructor")
    
class manager(programmer): 
    c = 3
   
    def __init__(self):
        super().__init__() # hmne ye likha hy ke tm parent ka bhi inctructor ko use kro i mean print kr do 
        print("This is manager constructor")
 
    
# o = employee()
# print(o.a)
# p = programmer()
# print(p.a , p.b)
m = manager()
print(m.a , m.b , m.c)


