class employee():
    a = 1
    
class programmer(employee): # sb employee wala agaya
    b = 2
    
class manager(programmer): #sb prgrammer plus employee ka agaya
    c = 3
    
o = employee()
print(o.a)
p = programmer()
print(p.a , p.b)
m = manager()
print(m.a , m.b , m.c)