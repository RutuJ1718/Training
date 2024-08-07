#Custom classes demonstrating inheritance:

# Single Inheritance
class Animal:
    def speak(self):
        return "Animal sound"

class Dog(Animal):
    def speak(self):
        return "Bark"

# Multiple Inheritance
class Walker:
    def walk(self):
        return "Walking"

class Flyer:
    def fly(self):
        return "Flying"

class Bird(Walker, Flyer):
    pass

# Multilevel Inheritance
class Organism:
    def live(self):
        return "Living"

class Mammal(Organism):
    def feed(self):
        return "Feeding"

class Human(Mammal):
    def think(self):
        return "Thinking"

# Usage
dog = Dog()
print(dog.speak())

bird = Bird()
print(bird.walk())
print(bird.fly())

human = Human()
print(human.live())
print(human.feed())
print(human.think())
