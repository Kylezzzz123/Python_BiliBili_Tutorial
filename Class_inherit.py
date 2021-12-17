class Person(object):   #Peson inherits class of object, object is a class
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(self.name, self.age)


class Student(Person):   # Student inherits all the methods from Person, so it can to get the method info(self)
    def __init__(self, name, age, stu_num): 
        super().__init__(name, age)   # super() is to get the Class Person's method  (self.name = name; self.age = age)
        self.stu_num = stu_num

class Teacher(Person):
    def __init__(self, name, age, teachofyear):
        super().__init__(name, age)
        self.teachofyear = teachofyear

stu = Student("Bonnie", 20, "1001")
teacher = Teacher("Tracy", 30, 10)

stu.info()
teacher.info()
 

'''
example: 

class A (object):
    pass

class B(obejct):
    pass

class C (A, B):
    pass

'''
