class employee :
    lang = "py"
    salary = 12000
    
    def __init__(self , name , salary , lang ):  # ye khud call hojata hy or isko call nahi krna prta isko dunder method kehty hen 
        self.name = name
        self.salary = salary 
        self.lang = lang
        
        
        print("i am dunder method")
        # koi bhi obj bny ga tw ye bar bar call hoga srf init dunder method
        
harry = employee("harry" , 130000 , "javascript")
# harry.name = "harry"
print(harry.salary, harry.lang , harry.name ) #this is a class attribute
# rohan = employee()
# print(rohan.salary, rohan.lang )