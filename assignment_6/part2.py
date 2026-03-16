import numpy as np

arr = []

n = int(input("Enter size of array: "))

for i in range(n):
    arr.append(float(input("Enter an element to add to the array: ")))

arr = np.array(arr)

x = 0
for i in arr:
    x += i

x /= n

num = 0
for i in arr:
    num += (i-x)**2

num /= n
s = num**.5

print (f"{s:.2f}")