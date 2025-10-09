# Create a base class called Animal

# Method: make_sound() → prints "Some generic animal sound"

# Create three subclasses:

# Dog → override make_sound() to print "Woof!"

# Cat → override make_sound() to print "Meow!"

# Cow → override make_sound() to print "Moo!"

# Write a function called animal_sound(animal) that takes an Animal object and calls make_sound() on it.

# Create a list of animal objects (Dog, Cat, Cow, etc.) and loop through them, passing each to animal_sound().

class animal:
    def make_sound(self):
        print("some generic animal sound")
class dog(animal):
    def make_sound(self):
        print("woof!")
class cat(animal):
    def make_sound(self):
        print("Meow!")
class cow(animal):
    def make_sound(self):
        print("Moo!")

dog=dog()
cat=cat()
cow=cow()
dog.make_sound()
cat.make_sound()
cow.make_sound()