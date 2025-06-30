#iska mtlb ye hy ke hm ek class ko
# dosry men inherit kr den ke us class
# ka sara data tw ayega or agr chahy tw new
# data bhi dal den 

class employee:
    company = "ITC" # class attribute 

    def show(self, name, salary):
        self.name = name
        self.salary = salary
        print(f"The name of employee is {self.name} and the salary is {self.salary}")
    def lang(self, name, lang):
        self.name = name
        self.lang = lang
        print(f"The name of employee is {self.name} and the language is {self.lang}")


class programmer(employee):
    company = "Found ITC"

    def lang(self, name, lang):
        self.name = name
        self.lang = lang
        print(f"The name of employee is {self.name} and the language is {self.lang}")


a = employee()
b = programmer()

# b.lang("harry", "py")
# print(b.name, b.lang)  # b.lang is a method, not a value — error ayega
a.company()# ye koi methid nahi hy jisko men call kron ye ek string hy isko print krna prega 
# b.show("harry", "12k")
# a.show("rohan", "12k")