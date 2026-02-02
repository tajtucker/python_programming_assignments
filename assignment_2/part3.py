# Write a program that repeatedly asks the user to enter three integers. Determine if the numbers form an increasing, decreasing, or neither sequence using if-elif-else. Print the odd numbers between the smallest and largest of the three values using a for loop. The program continues until the user enters "stop".

print("Enter three integers. Type 'stop' to exit.")
print()

while True:
    prompt = input("Enter three integers separated by spaces: ")
    if prompt == "stop":
        print("Program Terminated.")
        break
    
    numbers = prompt.split()

    numbers[0] = int(numbers[0])
    numbers[1] = int(numbers[1])
    numbers[2] = int(numbers[2])


    if numbers[0] < numbers[1] and numbers[1] < numbers[2]:
        print("The sequence is increasing.")
    elif numbers[0] > numbers[1] and numbers[1] > numbers[2]:
        print("The sequence is decreasing.")
    else:
        print("The sequence is neither increasing nor decreasing.")

    for x in range(min(numbers), max(numbers)):
        if x % 2 != 0:
            print(x, end=" ")
    print()