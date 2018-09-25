class Pets:
    Dogs = []
    def __init__(self, Dogs):
        self.Dogs = Dogs

class Dog:
    type = "mammals"
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.is_hungry = True

    def eat(self):
        self.is_hungry = False

dog_list = [Dog('tom',6),Dog("fletcher", 7),Dog("Larry", 9)]
my_dogs = Pets(dog_list)

print("I have " +  str(len(my_dogs.Dogs)) +" Dogs")
print()
for pet in my_dogs.Dogs:
    pet.eat()
    print("{} is {}.".format(pet.name, pet.age))
print()

print("And they're all {}, of course.".format(Dog.type))

Starving= False
for dog in my_dogs.Dogs:
    if dog.is_hungry:
        Starving = True

if Starving:
    print("My dogs are hungry.")
else:
    print("My dogs are not hungry.")
