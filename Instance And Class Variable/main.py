class Hero(): #template / class
    #class variable
    total = 0
    
    def __init__(self, inName, inClass, inSkill):
        # instance variable
        self.name = inName
        self.classes = inClass
        self.skill = inSkill
        Hero.total += 1
        print("Hero name "+inName)

riven = Hero("Riven", "Fighter", "Normal")
print(Hero.total)

garen = Hero("Garen", "Defender", "Easy")
print(Hero.total)




