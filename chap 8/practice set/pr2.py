# write a program to convert celcius to ferinhide

# F=(C× 9/5)+32 
# yhan hm jo function hy usme koi bhi variable de skty hen
def ferinhide(c):
    return c*(9/5)+32 #yhan hmen return hi likhna hy warna wo bs print krega ki calc nahi krega 

a = int(input("Enter your °C")) 
print(f"{round(ferinhide(a) , 2)}") 

#is se khali 2 number ayengy after decimal, lmba nai hoga 