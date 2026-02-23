# Compute 𝑒x: You already developed your factorial function in Part-1. You are required to use that function. Let the user input the value of 𝑥. Continue adding terms until the difference of successive terms is less than 0.001. Compare your answer with the Python "math.e ** x". You should show your results for 𝑥=1, 𝑥=2 and 𝑥=3.

import math
from assignment_3.part1 import factorial

def computeE(x):
    e = 1
    n = 1
    previous = 1

    while True:
        current = (x ** n) / factorial(n)

        if abs(current) < 0.001:
            break

        e += current
        n += 1
    
    return e

print(computeE(1))
print(computeE(2))
print(computeE(3))
print(math.e**1)
print(math.e**2)
print(math.e**3)