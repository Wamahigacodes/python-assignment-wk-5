# Python OOP Concepts Demonstration

This repository contains two simple Python programs that demonstrate fundamental Object-Oriented Programming (OOP) concepts.

## 📁 Files

1. **`superhero_demo.py`** - Demonstrates class creation, inheritance, and constructors
2. **`polymorphism_demo.py`** - Demonstrates polymorphism with different vehicle types

## 🦸‍♂️ Superhero Demo (Assignment 1)

This program shows how to create classes with constructors and implement inheritance.

### Concepts Demonstrated:
- **Class Creation**: Defining a `Superhero` class with attributes and methods
- **Constructors**: Using `__init__()` to initialize objects with unique values
- **Inheritance**: Creating a `TechHero` class that extends `Superhero`
- **Method Implementation**: Adding functionality through class methods

### Code Overview:
```python
class Superhero:
    def __init__(self, name, power):
        self.name = name
        self.power = power
    
    def use_power(self):
        return f"{self.name} uses {self.power}!"

class TechHero(Superhero):
    def __init__(self, name, power, gadget):
        super().__init__(name, power)
        self.gadget = gadget
    
    def use_gadget(self):
        return f"{self.name} uses {self.gadget}!"
```

### Usage:
```bash
python superhero_demo.py
```

### Expected Output:
```
Superman uses super strength!
Iron Man uses repulsor beams!
Iron Man uses Jarvis AI!
```

## 🚗 Polymorphism Demo (Activity 2)

This program demonstrates polymorphism by implementing the same method (`move()`) across different classes with unique behaviors.

### Concepts Demonstrated:
- **Polymorphism**: Different classes implementing the same method in different ways
- **Class Design**: Creating multiple classes with a consistent interface
- **Constructor Usage**: Initializing objects with specific attributes

### Code Overview:
```python
class Car:
    def __init__(self, model):
        self.model = model
    
    def move(self):
        return f"{self.model} is driving 🚗"

class Plane:
    def __init__(self, model):
        self.model = model
    
    def move(self):
        return f"{self.model} is flying ✈️"

class Boat:
    def __init__(self, model):
        self.model = model
    
    def move(self):
        return f"{self.model} is sailing ⛵"
```

### Usage:
```bash
python polymorphism_demo.py
```

### Expected Output:
```
Tesla is driving 🚗
Boeing is flying ✈️
Yacht is sailing ⛵
```

## 🎯 Learning Objectives

Through these examples, you can learn:

1. How to define classes in Python using the `class` keyword
2. How to use constructors (`__init__()`) to initialize objects
3. How inheritance works with the `super()` function
4. How polymorphism allows different objects to respond to the same method call differently
5. How to create and use class instances

## 🔧 Requirements

- Python 3.x
- No external dependencies

## 📚 Further Learning

Try modifying these examples by:
1. Adding more attributes to the classes
2. Creating additional subclasses
3. Implementing more methods
4. Experimenting with different polymorphic behaviors

These simple examples provide a foundation for understanding more complex OOP concepts in Python!
