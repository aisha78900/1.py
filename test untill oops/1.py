# n= int(input("Enter ur number: ")) 

# for i in range (1 , 11):
#     print(f"{n} * {i} = {n*i}")
    
# fruits = ["apple", "banana", "mango"]
# fruits.append("grape")
# print(fruits[2])

d = { "name" : "ayesha", "age" : 12 , "city" : "karachi"}

print(d["age"])


# Write a class BankAccount with:

# balance as an attribute (default 0)

# deposit(amount) method

# withdraw(amount) method

# Show updated balance after each operation

# class bank_account:
#     def __init__(self):
#         self.balance = 0
    
#     def deposit(self, amount):
#         self.balance += amount 
#         print(f"Deposited: {amount}, Updated Balance: {self.balance}")
    
#     def withdraw(self, amount):
#         if amount > self.balance:
#             print("Insufficient funds")
#         else:
#             self.balance -= amount
#             print(f"Withdrawn: {amount}, Updated Balance: {self.balance}")

# # Create an instance (object) of bank_account
# ac = bank_account()
# ac.deposit(1000)
# ac.withdraw(400)


class Employee:
    def __init__(self):
        self.__salary = 1000

e = Employee()
print(e.__salary)

