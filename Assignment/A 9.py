# Base class Animal
class Animal:
    # __init__ method to initialize the animal with name and species
    def __init__(self, name, species):
        self.name = name
        self.species = species

    # Method to return a generic sound
    def make_sound(self):
        return "Some generic sound"


# Derived class Dog that inherits from Animal
class Dog(Animal):
    # Override the make_sound method to return "Woof!"
    def make_sound(self):
        return "Woof!"

    # Method to return a string indicating the dog is fetching a ball
    def fetch(self):
        return f"{self.name} is fetching the ball."


# Sample Input
dog = Dog("Buddy", "Golden Retriever")

# Print the dog's sound and fetch behavior
print(dog.make_sound())  # Output: Woof!
print(dog.fetch())  # Output: Buddy is fetching the ball.
