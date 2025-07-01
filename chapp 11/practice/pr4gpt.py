
# ✅ Complex Number Class with + and * Overloading
class Complex:
    
    # 🔹 Jab object banate hain, to yeh function chalega
    def __init__(self, r, i):
        # 'self.r' = real part store karne ke liye
        # 'self.i' = imaginary part store karne ke liye
        self.r = r
        self.i = i

    # 🔹 Jab hum 2 objects ko '+' se add karein
    def __add__(self, other):
        # Dono objects ka r aur i add karo aur ek new object return karo
        return Complex(self.r + other.r, self.i + other.i)

    # 🔹 Jab hum 2 objects ko '*' se multiply karein
    def __mul__(self, other):
        # (a + bi)(c + di) = (ac - bd) + (ad + bc)i
        real_part = (self.r * other.r) - (self.i * other.i)
        imag_part = (self.r * other.i) + (self.i * other.r)
        return Complex(real_part, imag_part)

    # 🔹 Jab object ko print() karein, to yeh format use hoga
    def __str__(self):
        # Object ka output jaise: 4 + 6i
        return f"{self.r} + {self.i}i"


# ✅ Object banaye: c1 = 1 + 2i, c2 = 3 + 4i
c1 = Complex(1, 2)
c2 = Complex(3, 4)

# ✅ In dono ko add kar diya: (1+3, 2+4) = 4 + 6i
sum_result = c1 + c2

# ✅ In dono ko multiply kiya: (1+2i)*(3+4i) = -5 + 10i
mul_result = c1 * c2

# ✅ Print the results
print("Addition:", sum_result)      # Output: 4 + 6i
print("Multiplication:", mul_result) # Output: -5 + 10i
 