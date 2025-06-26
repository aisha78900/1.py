# problem 1 : make a programm of dictoany in which words hindi me hon or unki values ki english translation ho


# d= { 
#     "Aloo" : "Potato",
#    "Tamatar":"Tomato",
#    "Pyaaz":"Onion",
#     "Gajar" : "Carrot"
#     }

# ask = input("enter word you want meaninig? :" )
# print(ask[d]) 
# ye abhi bs key do ye value dega 

# probelm 2 usmen ye hoga ke hmen input lena hy or un numbers ko hmne once print krwana hy
# tw jb hm kisi ko once print krne ka bolen means ke wo set hoga 

# s = set()
# n= int(input (" Enter Your Number" )) 
# print(s.add(n))
# n= int(input (" Enter Your Number" )) 
# print(s.add(n))
# n= int(input (" Enter Your Number" )) 
# print(s.add(n))
# n= int(input (" Enter Your Number" )) 
# print(s.add(n))
# n= int(input (" Enter Your Number" )) 
# print(s.add(n))
# print(s)

# s = set()
# s.add(18)
# s.add("18")

# print(s)


s = set()
s.add(20)
s.add(20.0)
s.add('20') # length of s after these operations?

print(len(s))


#error
#4

# problem 5
# Create on empty dictionary. Allow 4 friends to
# enter theix' fovowrite language as 'yalues and use Reys as theis names. Assume that the names Are unique
d = {}
name = input("Enter Your name :")
lang = input("Enter your lang :")
d.update({ name : lang})

name = input("Enter Your name :")
lang = input("Enter your lang :")
d.update({ name : lang})

name = input("Enter Your name :")
lang = input("Enter your lang :")
d.update({ name : lang})

print(d)
