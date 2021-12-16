class Circle(object):
    def __init__(self, radius):
        self.radius = radius

    @property
    def diameter(self):
        return self.radius * 2
    @property
    def area(self):
        return self.radius * self.radius * 3.14

my_circle = Circle(2)

list = [
    "Your radius is {}".format(my_circle.radius),
    "Your diameter is {}".format(my_circle.diameter), 
    "Your Area of circle is {}".format(my_circle.area)
]

for lists in list:
    print(lists)

