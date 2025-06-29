# create a class capable of finding sq rott and cube

class calc:
    def __init__(self , n):
        self.n = n
        
    def squareroot(self):
        print(f"sq root of {n} is {self.n**1/2}")
        
    def cube(self):
        print(f"cube  of {n} is {self.n*self.n*self.n}")
        
    def square(self):
        print(f"square  of {n} is {self.n*self.n}")

n = int(input("enter ur numb: "))
c = calc(n) # n ko is functio me again dena prega ke ye wala n hy jo calc me use kro phr hm isko nechy caal krengy
c.squareroot()
c.square()
c.cube()
