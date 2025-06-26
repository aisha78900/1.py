n = int(input("Enter a number: "))  
# User se number input lena (integer type)

for i in range(2, n):  
    # Loop 2 se shuru ho kar n-1 tak chalega
    # Kyunke 1 aur n khud prime number ke liye allowed hote hain
    # Hum check kar rahe hain: kya koi aur number beech mein n ko divide karta hai?

    if (n % i) == 0:  
        # Agar n ko i se divide karne par remainder 0 aa gaya
        # Matlab: n kisi aur number se divide ho gaya
        # To phir n prime number nahi hai
        
        print("Number is not prime")  
        break  
        # Yahan 'break' ka matlab hai loop ko turant roko
        # Hume pata chal gaya ke number prime nahi hai, to ab aage check karne ki zarurat nahi
else:
    # Ye 'else' sirf tab chalta hai jab loop kabhi 'break' na ho
    # Matlab: agar upar wala if kabhi true nahi hua
    # To matlab koi bhi number n ko divide nahi kar saka
    # To n prime number hai

    print("Number is prime")
    
    
#check weather the number is prime or not 

n = int(input("enter your number: "))

for i in range(2 , n) :
    if(n%i == 0): # % ye ek operator hy jo reminder btata hy
        print("Not prime number")
        break 
    
else:
    print("prime num")