# Greet all person in list whose name starts with "S"

names = ["Rajnish", "Shyam", "Sohan", "Sweta", "Sweety", "Radha", "Sampoo"]

for item in names:
    if (item.lower().startswith("s")):
        print(f"Good morning, {item} !")
    
