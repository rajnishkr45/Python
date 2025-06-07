# 📘 Python Chapter 8: Functions & Recursion

🗓️ Date: June 7, 2025

---

## 🔥 What I Learned

### ✅ Functions in Python

* Functions are blocks of reusable code that perform a specific task.
* Created using the `def` keyword.

```python
def greet(name):
    print(f"Hello, {name}!")
```

### 💡 Function Arguments

* **Positional Arguments**: Default order-based arguments.
* **Keyword Arguments**: Pass values using keys.
* **Default Arguments**: Provide default value if none is given.
* **Variable-length Arguments**: Use `*args` and `**kwargs`.

```python
def add(a, b=10):
    return a + b
```

### ⟳ Return Statement

* Use `return` to send back a result from a function.

```python
def square(x):
    return x * x
```

---

## 🔄 Recursion

* A function calling itself.
* Needs a **base case** to avoid infinite loops.

```python
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)
```

### ⚠️ Recursion Limit

* Python has a recursion depth limit (\~1000).
* For large problems, use loops or math formulas instead.

---

## 📌 Practice Example

```python
def sum_natural(n):
    if n == 1:
        return 1
    return n + sum_natural(n - 1)

num = int(input("Enter a number: "))
print(f"Sum of first {num} natural numbers is: {sum_natural(num)}")
```

### ❌ Error Faced:

```text
RecursionError: maximum recursion depth exceeded
```

> Fixed by using the formula: `n * (n + 1) // 2`

---

## ✅ Summary

| Concept   | Description                         |
| --------- | ----------------------------------- |
| Function  | A block of reusable code            |
| Recursion | Function calling itself             |
| Base Case | Ending condition in recursion       |
| return    | Used to send output from a function |

---