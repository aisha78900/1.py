class number:
    def __init__(self , n):
        self.n = n
    def __add__(self , num):
        return self.n + num.n 
    
a = number(1)
b = number(2)
print(a + b)

# Yeh class `number` do number objects ko add karne ke liye banayi gayi hai. 
# Jab object banate hain (`a = number(1)`), to uska number `self.n` me store 
# ho jata hai. `__add__` ek special method hai jo `+` operator ko custom banata hai.
# Jab hum `a + b` likhte hain, to Python `a.__add__(b)` ko call karta hai, jahan `a` 
# ka number `self.n` hota hai aur `b` ka number `num.n`. Yeh method dono numbers ko add 
# karke result return karta hai. Is tarah hum custom objects ke sath bhi `+` ka use kar 
# sakte hain jaise normal numbers ke sath karte hain.
