class emp:

    @property 
    def name(self):
        return f"{self.fname} {self.lname}"
    @name.setter #hm setter ko tb use krty hen jb hmen koi condition deni ho 
    def name(self , value):
        self.fname = value.split(" ")[0]   #value ka part 1 le lo
        self.lname = value.split(" ")[1]   #value ka part 2 le lo 

e = emp()
e.name="Harry Khan"
print(e.fname )