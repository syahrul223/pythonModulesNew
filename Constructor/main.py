class Hero():
    def __init__(self, inName, inClass, inSkill):
        self.name = inName
        self.classes = inClass
        self.skill = inSkill

# method 1 
syahrul = Hero("Syahrul", 12, "Rekayasa Perangkat Lunak")
# method 2
guestName = "Name"
guestClass = 0
guestSkill = "Skill"

guest = Hero(guestName, guestClass, guestSkill)

print(guest.__dict__)
print(syahrul.__dict__)
    