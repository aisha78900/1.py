# create a class pets from a class animal and further create a class dog from pets and add a bark method in it 

class animal():
    pass
class pet(animal):
    pass
class dog(pet):
    def bark(self , name):
        self.name = name
        print(f"{self.name} is barking")
        
b = dog()
b.bark("Tommy")