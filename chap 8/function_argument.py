def goodday(name):
    print("good day, " , name)
    
goodday("harry") 

# agr hmen 2 print krwany hon tw hm ese kr skty hen ke hm 2 variable de den function me like this 
def goodday(name , ending ):
    print("good day, " , name)
    print(ending)
    
# goodday("harry" , "Thanks") 

# -------------------Return--------------------------
# agr hm function kisi variable men daly tw hmen return use krna hota hy wrna none ata hy 

# jese 
def goodday(name , ending ):
    print("good day, " , name)
    print(ending)
    return "done" 


a = goodday("harry" , "Thanks") 
print(a)