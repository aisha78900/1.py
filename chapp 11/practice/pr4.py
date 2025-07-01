# create a class complex represent complex 
# number along with overload
# operator + and * which adds 
# and multiplies them 

class complex :
    def __init__(self_init , r , i ): #jo self hy wo ek obj ke lie likha hwa taky jb koi neechy obj bnaye tw usmen value de sky like self = harry and then harry.r and harry.i
        self_init.r = r # ye bn gaya c1.r = 1
        self_init.i = i # ye bn gaya c1.i = 2 same as c 2
        
    def __add__(self1  , self2): #self first 
        return complex(self1.r + self2.r , self1.i + self2.i) #isne oper se complex lia or us me variable die 
    # isme jo self hy usne oper se r lia and self2 ne bhi esi hi kia 
    def __str__(self_str):
        return f"{self_str.r} + {self_str.i}i"
    
c1 = complex(1 , 2) #jb hm c1 ko call krty hen tw hm init function ko call kr rhy like self
# ko c1 bna dia and r = 1 and i = 2
c2 = complex(3 , 4) # same as c1 

# ab jb isko c1 and c2 ki value mil gaye tw ye gya add ke pass ke dekho mjhy c1 bhi
# mil gya and c2 bhi mil gya ab men add krna 
# chata ho tw add ne kia kia c1 ko as a self1 le lia and c2 ko as a self2 le lia
d = c1 + c2

print(d)


# __str__(self) ek special method hota hai jo 
# define karta hai ke jab koi object print() ho, to wo kis format me nazar aaye.

# Jab print(object) likha jata hai, 
# Python automatically object.__str__() call karta hai.



