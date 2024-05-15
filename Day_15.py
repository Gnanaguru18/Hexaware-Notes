# Abstract or Interface
# Force other class to implement certain methods
# Autocomplete
from abc import ABC, abstractmethod
 
 
# Abstract class / Interface
class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass
 
    @abstractmethod
    def move(self):
        pass
 
 
class Dog(Animal):
    def make_sound(self):
        print("Woof Woof")
 
    def move(self):
        print("Runnning... 🐕")
 
    def jump(self):
        print("Jumps 🦘")
 
 
maxy = Dog()
maxy.move()

# Task - Bird class that implements our Animal abstract class

class Bird(Animal):
    def make_sound(self):
        print("ka ka")
    def move(self):
        print("Flying")

Crow=Bird()
Crow.move()