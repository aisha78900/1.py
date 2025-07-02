# agr hm koi input den as int or jb user 
# int ki jaga str likh de tw ye
# kro ke tm error na dikha ke exception likh do 
try:
    a = int(input("Enter numb: "))
    print(a)
    
    
except ValueError as v:
    print("heyy")
    print(v)
except Exception as e:
    print(e) # agr hm ye na likhen tw code yhan hi error de kr chlna bnd hojaega
    
    
# ye error nahi dega blky btayea ke ye msla hy code me

print("Thank you") 