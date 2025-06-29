# ek class bnoa attribute a kr ke phr ek obj bnao is se and set a directly sing object.a . will it change class attribute?


class demo:
    a = 2
    
o = demo()
o.a = 0 #instance attribute is set
print(o.a) # ye ek instance attribute set hogya 
print(demo.a) # ye class attribute change nahi hoga 