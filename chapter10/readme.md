# 📘 Python Learning Journal

## 🗓️ Date: 10/06/2025

### ✅ Topics Covered Today:

* **Classes and Objects**
* **Constructors (`__init__` method)**
* **Dunder Methods (Magic Methods)**

---

## 🔹 Classes and Objects

**Class** is a blueprint for creating objects. An **object** is an instance of a class.

### 🔸 Example:

```python
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

my_car = Car("Toyota", "Corolla")
print(my_car.brand)  # Output: Toyota
```

---

## 🔹 Constructor (`__init__` Method)

* The `__init__` method is called automatically when a new object is created.
* It is used to initialize object attributes.

### 🔸 Example:

```python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

s1 = Student("Alice", 21)
print(s1.name, s1.age)  # Output: Alice 21
```

---

## 🔹 Dunder Methods (Magic Methods)

* These are special methods that start and end with double underscores `__`.
* Used to override default behavior of objects (like printing, comparing, etc).

### 🔸 Common Dunder Methods:

* `__init__` → Constructor
* `__str__` → String representation
* `__len__` → Length of object
* `__repr__` → Official string representation
* `__eq__` → Equality comparison

### 🔸 Example:

```python
class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def __str__(self):
        return f"Book: {self.title}"

    def __len__(self):
        return self.pages

b1 = Book("Python Basics", 300)
print(b1)           # Output: Book: Python Basics
print(len(b1))      # Output: 300
```

---

## 🧠 Summary:

* Classes group related data and functions.
* `__init__` sets up initial object state.
* Dunder methods make classes behave like built-in types.
