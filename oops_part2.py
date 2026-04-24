# OOPS PART - 2

# 3. Polymorphism (live/live)

# 1. Method Overriding
# 2. Method Overloading (python doesn't support method overloading by default)


# 1. Method Overriding

class Animal:
    def sound(self):
        print("Animal makes sound")

class Dog(Animal):
    def sound(self):
        print("Dog Barks")
    # pass

class Cat(Animal):
    def sound(self):
        print("Cat Meow")
        

animals = [Dog(), Cat()]

# for cls in animals:
#     cls.sound()
    
    
# 2. Method Overloading

def add(a, b):
    print(a+b)

def add(a, b, c=0):
    print(a+b+c)
    
# add(10, 40)
# add(10, 30, 20)


# 4. Abstraction

from abc import ABC, abstractmethod

class Vehicle(ABC):
    
    @abstractmethod
    def start(self):
        pass

class Car(Vehicle):
    
    def start(self):
        print("Key dedected, start the car")

class Bike(Vehicle):
    
    def start(self):
        print("Key dedected, start the Bike")
    
    def stop(self):
        print("Key out of range - stop vehicle")

# car = Car()
# print(car.start())

bike = Bike()
print(bike.start())
print(bike.stop())



