class employee :
    lang = "py"
    salary = 12000
    
harry = employee()
harry.name = "harry"
print(harry.salary, harry.lang , harry.name ) #this is a class attribute

rohan = employee()
rohan.name = "rohan" # this is instance attribute
print(rohan.name , rohan.salary , rohan.lang)

# here lang and salary are clas attributes and name is instance(object) attribute 