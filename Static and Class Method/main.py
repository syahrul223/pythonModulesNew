class Hero:

    # private class variable
    __jumlah = 0
    
    def __init__(self, name):
        self.__name = name
        Hero.__jumlah += 1

    # method ini hanya berlaku untuk object
    def getJumlah(self):
        return Hero.__jumlah

    # method ini tidak berlaku untuk object tapi berlaku untuk class
    def getJumlah1():
        return Hero.__jumlah

    # method static (decorator) nempel ke objek dan class
    @staticmethod
    def getJumlah2():
        return Hero.__jumlah

    # method class
    @classmethod
    def getJumlah3(cls):
        return cls.__jumlah


sniper = Hero('sniper')
print(Hero.getJumlah2())
riki = Hero('rikimaru')
print(sniper.getJumlah2())
pudge = Hero('pudge')
print(Hero.getJumlah3())