# Find the line number in which word "python" is present

word = "python"
i = 1
with open("log.txt", "r") as f:
    lines = f.readlines()

for line in lines:
    if "python" in line:
        print(f"python word found in line number {i}")
else:
    print("No python is not present")
