# create a class programmer which store data of employess at microsoft

class programmer:
    company = "microsoft"
    def __init__(self , name , salary ):
       self.name = name
       self.salary = salary
       
    
p = programmer("Harry" , "10k")
print(p.name , p.salary)
r = programmer("Rohan" , 120000)
print(r.name , r.salary)
