import numpy as np

N = int(input("Enter the number of values: "))

arr = np.zeros(N)

for i in range(N):
    arr[i] = float(input("Enter a number: "))

total = 0
for i in range(N):
    total += arr[i]

mean = total / N

sum_sq = 0
for i in range(N):
    sum_sq += (arr[i] - mean) ** 2

s = (sum_sq / N) ** 0.5

print("Standard deviation:", s)