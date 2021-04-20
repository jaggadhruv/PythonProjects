print("This is Polymorphism Script")

class Dog():

    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + " Woof Woof"


class Cat():

    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + " Meaow"



# ---------------------------------------------------------------
niko = Dog("Niko")
felix = Cat("Felix")

print(niko.speak())
print(felix.speak())

