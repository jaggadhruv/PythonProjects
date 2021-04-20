print("This is Object Oriented Programming Script")

class Animal():

    def __init__(self):
        print("Animal Created")

    def who_am_I(self):
        print("I am an Animal")

    def eat(self):
        print("I am Eating")

# Calling base class in derived class
class Dog(Animal):
    # Class object attributes
    # Same for any instances or methods of the class

    species = "Mammel"

    #   Init is used for attribute setting {Constructor of the class}
    def __init__(self,breed, age, colour):
        Animal.__init__(self)
        print("Dog is Created")

        self.breed = breed
        self.age = age
        self.colour = colour

    #   Methods of the Dog Class
    def bark(self,number):
        print(f"Woof, My breed is {self.breed} and My Number is {number}")


class Circle:

    #   Attribute
    pi = 3.147

    def __init__(self, radius = 1):
        self.radius = radius

    #   Method
    def get_circumfrence(self):
        return 2 * Circle.pi * self.radius

# --------------------------------------------------------

my_animal = Animal()
my_animal.who_am_I()
my_animal.eat()


my_dog = Dog(breed="Lab", age=5.5, colour="Magenta")
print(type(my_dog))
print(my_dog.breed,"|",my_dog.age,"|",my_dog.colour,"|",my_dog.species)
my_dog.bark(21)
my_dog.who_am_I()

my_circle = Circle(radius=30)
circumference_circle = my_circle.get_circumfrence()
print(circumference_circle)