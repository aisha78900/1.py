a = 89
def fun():
    global a #ye lgany se hm global 
    # variable ko all over hi change kr skty hen 
    a = 3
    print(a)
    
    
fun()
print(a)