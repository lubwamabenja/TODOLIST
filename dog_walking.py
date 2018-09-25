class Pets:
    Dogs = []
    def __init__(self, Dogs):
        self.Dogs = Dogs
    def walk(self):
        for x in self.Dogs:
            print(x.walk())

class Dog:
    type = "mammals"
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.is_hungry = True

    def eat(self):
        self.is_hungry = False

    def walk(self):
        return "{} is walking!".format(self.name)

dog_list = [Dog('tom',6),Dog("fletcher", 7),Dog("Larry", 9)]
my_dogs = Pets(dog_list)
my_dogs.walk()