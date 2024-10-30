## Assignment 1: Static Methods##
class MathOperations:
    @staticmethod
    def add_numbers(a, b):
        return a + b

    @staticmethod
    def multiply_numbers(a, b):
        return a * b


sum_result = MathOperations.add_numbers(4, 3)
product_result = MathOperations.multiply_numbers(5, 7)

print(f"Sum: {sum_result}")
print(f"Product: {product_result}")

##Assignment 2: Class Methods

class Person:
    count = 0

    def __init__(self):
        Person.count += 1

    @classmethod
    def get_count(cls):
       return cls.count

person1 = Person()
person2 = Person()
person3 = Person()

print(f"Number of Person instances created: {Person.get_count()}")

## Assignment 3: Using Both Static and Class Methods

class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(celsius):
        return (celsius * 9/5) + 32

    @classmethod
    def info(cls):
        return "Temperature Converter: Use the celsius_to_fahrenheit method to convert Celsius to Fahrenheit."


celsius_temp = 25
fahrenheit_temp = TemperatureConverter.celsius_to_fahrenheit(celsius_temp)
conversion_info = TemperatureConverter.info()

print(f"{celsius_temp}°C is {fahrenheit_temp}°F")
print(conversion_info)

##Assignment 4: Single Inheritance
class Animal:
    def sound(self):
        print("Animal sound")

class Dog(Animal):
    def sound(self):
        print("Bark")

animal = Animal()
animal.sound()

dog = Dog()
dog.sound()

## Assignment 5: Multiple Inheritance

class Bird:
    def fly(self):
        print("Flying")

class Fish:
    def swim(self):
        print("Swimming")

class Duck(Bird, Fish):
    def quack(self):
        print("Quack")

duck = Duck()
duck.fly()
duck.swim()
duck.quack()

##Assignment 6: Abstract Class

from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

circle = Circle(5)
rectangle = Rectangle(4, 6)

print(f"Area of the circle: {circle.area():.2f}")
print(f"Area of the rectangle: {rectangle.area():.2f}")

## Assignment 7: Encapsulation

class BankAccount:
    def __init__(self, initial_balance=0):
        self._balance = initial_balance  # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"Deposited: ${amount:.2f}. New balance: ${self._balance:.2f}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
            print(f"Withdrew: ${amount:.2f}. New balance: ${self._balance:.2f}")
        else:
            print("Insufficient funds or invalid amount.")

    def get_balance(self):
        return self._balance

account = BankAccount(100)
account.deposit(50)
account.withdraw(30)
print(f"Current balance: ${account.get_balance():.2f}")

## Assignment 8: Polymorphism with Method Overriding

class Cat:
    def speak(self):
        print("Meow")

class Dog:
    def speak(self):
        print("Woof")

cat = Cat()
dog = Dog()

cat.speak()
dog.speak()

# Assignment 9: Polymorphism with Method Overloading
class Calculator:
    def add(self, a, b, c=0):
        return a + b + c


calculator = Calculator()


sum_two = calculator.add(5, 10)
print(f"Sum of 5 and 10: {sum_two}")  # Output: Sum of 5 and 10: 15


sum_three = calculator.add(5, 10, 15)
print(f"Sum of 5, 10, and 15: {sum_three}")

##Assignment 10: Multilevel Inheritance

class LivingBeing:
    def breathe(self):
        print("Breathing")

class Mammal(LivingBeing):
    def walk(self):
        print("Walking")

class Human(Mammal):
    def think(self):
        print("Thinking")


human = Human()
human.breathe()
human.walk()
human.think()