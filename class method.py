class Student:
    home_town = "Tokyo"
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print("I am eating")

    def method():
        print("I am using method")

    def cm(cls):
        print("I am using classmehtod")


print(Student.home_town)
stu1 = Student("Bonnie", 20)
stu2 = Student("Tracy", 22)

print(stu1.home_town)
print(stu2.home_town)

Student.home_town = "Hong Kong"
print(stu1.home_town)
print(stu2.home_town)

Student.method()
# Student.cm()                     #Error ?????  need to input something in cm()???? 