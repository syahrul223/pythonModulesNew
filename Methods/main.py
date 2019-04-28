class People:
    # class variable
    count = 0
    def __init__(self, inname, inage, incity):
        # instance variable
        self.name = inname
        self.age = inage
        self.city = incity
        People.count += 1

    # method with no return (void)
    def identity(self): 
        print("My name is "+ self.name)

    # method void with argumen/params
    def ages(self, year):
        self.age = year - self.age

    #method with return argumen
    def getAges(self):
        return self.age

people1 = People("John", 22, "Mexico")

people1.identity()
people1.ages(2019)
print("and was born in " + str(people1.getAges()) + " at " + people1.city)
