from collections import namedtuple


class Student: 
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def eat(self):
        print(self.name + " is eating")


stu1 = Student("Bonnie", 20)  # add an variable for a class
stu2 = Student("Tracy", 22)

stu1.eat()
stu2.eat()

stu1.gender = "Female"    #we can add an element into a method in a class, this is called dynamic
print(stu1.name, stu1.gender)

def show():
    print("This is a function")

stu1.game = show   #link the function show() to stu1, and set stu1.game is function show
stu1.game()

