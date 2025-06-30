# create a class employee and add salary and increment properties to it 
# 

class employee:
    salary = 230
    increment = 20
    
    @property
    def salarafterincrement(self):
        return (self.salary + self.salary*(self.increment/100))
    increment.setter
    def increm

e = employee()
print(e.salarafterincrement)


# Note: @property aur @property.setter dono methods ko function 
# ki tarah call nahi kiya jata — @property ko 
# variable ki tarah read kiya jata hai aur @setter
# ko assignment (=) ke through use kiya jata hai.