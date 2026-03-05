# Write a program that reads a sequence of integers into a NumPy array and that computes the alternating sum of all elements in the array. For example, if the program is executed with the input data 
# 1 4 9 16 9 7 4 9 11 then it computes 1-4+9-16+9-7+4-9+11 = -2


import numpy as np

nums = list(map(int, input("Enter integers separated by spaces: ").split()))

arr = np.array(nums)

alt_sum = 0

for i in range(len(arr)):
    if i % 2 == 0:
        alt_sum += arr[i]
    else:
        alt_sum -= arr[i]

print("Alternating sum:", alt_sum)