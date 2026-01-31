# Write a Python program that performs the following tasks:
# 1.	Prompt the user to enter two floating-point numbers separated by a space.
# 2.	Read the input using the split() method and convert the values to floats.
# 3.	Calculate and display the sum, product, and absolute difference of the two numbers, each formatted to two decimal places.
# 4.	Display the two numbers in ascending order, formatted to one decimal place, using the min() and max() functions (without using if, elif, or else statements).
# 5.	Determine whether the integer part of the first number is divisible by the integer part of the second number and display True or False.

prompt = input("Enter two floating-point numbers separated by a space: ")
number = prompt.split()

value1 = float(number[0])
value2 = float(number[1])

sum = value1 + value2
print(f"Sum: {sum:.2f}" )

product = value1 * value2
print(f"Product: {product:.2f}" )

absolute_diff = abs(value1 - value2)
print(f"Absolute Difference: {absolute_diff:.2f}" )

small_number = min(value1, value2)
large_number = max(value1, value2)
print(f"{small_number:.1f}, {large_number:.1f}")

divisible = int(value1) % int(value2) == 0
print(divisible)