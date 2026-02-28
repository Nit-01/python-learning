from abc import ABC ,abstractmethod

class Animal:
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        print("Dog Barks")

d=Dog()
d.sound()