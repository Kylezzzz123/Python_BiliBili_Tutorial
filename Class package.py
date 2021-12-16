class Car:
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        print(f"Your {self.brand} is started")


Your_car = Car('BMW')
Your_car.start()



class Student:
    def __init__(self, name, age):
        self.name = name
        self.__age = age
    def show(self):
        print(self.name, self.__age)   # __ means you don't need to access to age, we don't want people to acces to age, but you can do it, but not nessesary  

student = Student("Bonnie", 20)
student.show()

print(dir(student)) 
print(student._Student__age)   # we can add _ in front of class in order to show the age 

