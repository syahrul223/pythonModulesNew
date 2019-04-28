class Student:
    # class public variable
    total = 0
    # class private variable
    __name = "privateName"
    # class protected variable
    _class = "protectedClass"

    def __init__(self, name, studClass):
        self.name = name
        self.studClass = studClass
        self.privateName = Student.__name
        self.protectedClass = Student._class

student1 = Student("Syahrul", "XII RPL 1")

print(student1.__dict__)
print(student1._class) # <--- this will fine
print(student1.__name) # <--- this will error
    