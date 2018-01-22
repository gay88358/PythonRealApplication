class Animal:
    def __init__(self, name):
        self._name = name
    
    def bark(self):
        print("...")

class Dog(Animal):
    def __init__(self, name):
        Animal.__init__(self, name)
    
    def bark(self):
        print(self._name + ": Woof! Woof!")

class Cat(Animal):
    def __init__(self, name):
        Animal.__init__(self, name)
    
    def bark(self):
        print(self._name + ": Meow!")
    
animals = [Cat("mimi"), Dog('jerry')]

for animal in animals:
    animal.bark()