# make a calculator which will calculate the square and cube root of a number
import math


class Calculator:
    def cubeRoot(self, num):
        return math.pow(num, 1 / 3)

    def squareRoot(self, num):
        return math.pow(num, 1 / 2)


calc = Calculator()

print(calc.cubeRoot(27))
print(calc.squareRoot(64))
