class Hero:
    def __init__(self, name, health, armor):
        self.name = name
        self.__health = health
        self.__armor = armor
        # self.info = "name {} : \n\thealth: {}".format(self.__name, self.__health)

    @property
    def info(self):
        return "name {} : \nhealth: {}".format(self.name, self.__health)

    @property
    def armor(self):
        pass

    @armor.getter
    def armor(self):
        return self.__armor

    @armor.setter
    def armor(self, input):
        self.__armor = input

axe = Hero('Axe', 300, 50)

print('merubah info')
print(axe.info)
axe.name = 'enigma'
print(axe.info)
print('=' * 10)
print('getter dan setter untuk __armor')
print(axe.armor)
print(axe.__dict__)
axe.armor = 200
print(axe.armor)
print(axe.__dict__)

