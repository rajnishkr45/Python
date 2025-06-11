# 📘 Python Learning Journal

## 🗓️ Date: 11/06/2025

### ✅ Topics Covered Today:

* **Inheritance and abstraction**
* **Super function (`super()` method)**

---

## 🎓 Inheritance in Python

Inheritance allows a class (child/derived) to inherit properties and behaviors (methods) from another class (parent/base).

### ✅ Example:

```python
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

obj = Dog()
obj.speak()  # Inherited from Animal
obj.bark()   # Defined in Dog
```

### 🔹 Types of Inheritance:

* Single Inheritance
* Multiple Inheritance
* Multilevel Inheritance
* Hierarchical Inheritance
* Hybrid Inheritance

---

## 🔬 Abstraction in Python

Abstraction means hiding implementation details and showing only the essential features of the object.
In Python, abstraction can be achieved using **abstract base classes** from the `abc` module.

### ✅ Example:

```python
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

class Car(Vehicle):
    def start(self):
        print("Car is starting...")

c = Car()
c.start()
```

* Abstract classes cannot be instantiated.
* Any class inheriting from an abstract class must implement all abstract methods.

---

## 🔄 `super()` Function

The `super()` function is used to call methods from a parent class.
It is especially useful in inheritance and when overriding methods.

### ✅ Example:

```python
class Parent:
    def show(self):
        print("This is Parent class")

class Child(Parent):
    def show(self):
        super().show()
        print("This is Child class")

obj = Child()
obj.show()
```

### 🔹 Output:

```
This is Parent class
This is Child class
```

---

## 📈 Summary:

* Inheritance helps reuse code and build relationships between classes.
* Abstraction helps in designing clean and maintainable interfaces.
* `super()` is useful for accessing base class methods and constructors.

---

## 📚 Practice Task:

* Implement a `Shape` abstract class with an abstract method `area()`.
* Create `Rectangle` and `Circle` classes that inherit and implement the `area()` method.

---

Happy Coding! 🚀
