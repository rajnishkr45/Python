# 📘 Chapter 7: Loops in Python

🗓️ **Date:** 6th June 2025
📚 **Chapter:** 7
📌 **Topic:** Loops


Today I learned about **loops** in Python and practiced lots of questions.
Loops allow us to repeat a block of code multiple times, making programs more efficient.

---

## 🔁 Types of Loops

### 1. while Loop

Repeats as long as the condition is `True`.

```python
i = 0
while i < 5:
    print(i)
    i += 1
```

### 2. for Loop

Used to iterate over a sequence such as a list, tuple, string, or range.

```python
for i in range(5):
    print(i)
```

---

## 🔂 Loop Control Statements

### break Statement

Stops the loop immediately.

```python
for i in range(10):
    if i == 5:
        break
    print(i)
```

### continue Statement

Skips the current iteration and moves to the next.

```python
for i in range(5):
    if i == 2:
        continue
    print(i)
```

### else with Loop

Executes after the loop ends normally (not interrupted by `break`).

```python
for i in range(3):
    print(i)
else:
    print("Loop completed successfully.")
```

---

## 🔄 Common Use Cases

* Traversing lists, strings, tuples
* Automating repetitive tasks
* Filtering or validating data
* File reading and writing

---

## ✅ Summary

* `for` loop → used when number of iterations is known.
* `while` loop → used when looping condition depends on logic.
* `break`, `continue`, and `else` enhance loop control.


