# create a class employee and add salary and increment properties to it 
# 

class employee:
    salary = 230
    increment = 20
    
    @property
    def salarafterincrement(self):
        return (self.salary + self.salary*(self.increment/100))
    
    @salarafterincrement.setter
    def salarafterincrement(self , salary):
        self.increment = ((salary/self.salary) - 1)*100
        
      
e = employee()
e.salarafterincrement = 380
print(e.increment)


# Note: @property aur @property.setter dono methods ko function 
# ki tarah call nahi kiya jata — @property ko 
# variable ki tarah read kiya jata hai aur @setter
# ko assignment (=) ke through use kiya jata hai.