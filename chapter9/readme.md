# 📂 Python Journey

## 📅 Chapter: File I/O in Python

## 🗓️ Date: 09/06/2025

---

### ✅ Topics Covered:

* Opening and reading files
* Writing and appending to files
* Using `with` statement
* File modes (`r`, `w`, `a`, `r+`, etc.)
* Handling file errors

---

### 📘 Concepts Learned:

#### 🔹 Opening a File:

```python
file = open("example.txt", "r")  # Open file for reading
```

#### 🔹 Reading From a File:

```python
content = file.read()
print(content)
file.close()
```

#### 🔹 Writing To a File:

```python
file = open("example.txt", "w")
file.write("Hello, World!\n")
file.close()
```

#### 🔹 Appending To a File:

```python
file = open("example.txt", "a")
file.write("Adding a new line.\n")
file.close()
```

#### 🔹 Using `with` Statement (Best Practice):

```python
with open("example.txt", "r") as file:
    data = file.read()
    print(data)
# No need to call file.close()
```

#### 🔹 Read Lines One by One:

```python
with open("example.txt", "r") as file:
    for line in file:
        print(line.strip())
```

#### 🔹 Modes Summary:

| Mode | Meaning           |
| ---- | ----------------- |
| 'r'  | Read only         |
| 'w'  | Write (overwrite) |
| 'a'  | Append            |
| 'r+' | Read and Write    |

---

### ⚠️ Common Errors:

* `FileNotFoundError`: Trying to open a file that doesn't exist in read mode.
* `PermissionError`: Lack of permissions to access the file.
* `ValueError`: Using a closed file object.

---

### 🚀 Mini Project Idea:

**High Score Tracker**

* Read and write the highest game score to a file.
* Update the file only if the new score is higher.

```python
import random

def game():
    return random.randint(1, 100)

score = game()

try:
    with open("highscore.txt", "r") as file:
        high_score = int(file.read().strip() or 0)
except FileNotFoundError:
    high_score = 0

if score > high_score:
    with open("highscore.txt", "w") as file:
        file.write(str(score))
    print(f"🏆 New High Score: {score}")
else:
    print(f"Score: {score} | High Score: {high_score}")
```


✨ *Learning one line at a time, one bug at a time!* ✨
