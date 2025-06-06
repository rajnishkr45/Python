"""
    *
  * * *
* * * * *

"""

n = int(input("Enter the number of rows: "))
# j_max = 2 * n

# for i in range(1, n + 1):
#     for j in range(1, j_max):
#         if j <= n - i or j >= n + i:
#             print(" ", end="")
#         else:
#             print("*", end="")
#     print("")

# Method 2

for i in range(1, n + 1):
    print(" " * (n - i), end="")
    print("*" * (2 * i - 1), end="")
    print("")