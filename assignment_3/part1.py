# Write a function called factorial that takes an integer and returns an integer. It calculates factorial of the input argument. For example, factorial(5) returns 120 and factorial(6) returns 720. 

def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

for r in range(1, 11):
    print(factorial(r))