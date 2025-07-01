class employee :
    lang = "py"
    salary = 12000
    
    def getinfo():
        print(f"the language is {self.lang} the salary is {self.salary}")
    @staticmethod #is se ye self nahi lega q ky is me hmen koi object property nahi chai 
    def greet():
        print("good morning")
    
harry = employee()
harry.name = "harry"
print(harry.salary, harry.lang , harry.name ) #this is a class attribute
harry.getinfo() #employee.getinfo(harry)
harry.greet()
#self se hm ek object pass krwaty hen 


#hm koi bhi method bnaye hmen ek self dena prta hy jo class meo agr tw 
# classs blue print hoti hen class me class atribute hen and instance attribute hen 
# yhan harry ek object hy or agr hm instane attribute den tw uska mtlb ye hwa ke bs us object me hiooga sb me nahi hoga wo 