# Write a Python program that performs the following tasks:
# 1.	Create three tuples: core_tuple, elective_tuple, and capstone_tuple, each containing course numbers as strings.
# 2.	Print the contents of each tuple, the number of courses in each using the len() method, and the first and last courses using indexing.
# 3.	Display the second and third elective courses using slicing.
# 4.	Check if "DATA 5400" is in core_tuple using the in operator and print True or False.
# 5.	Demonstrate the immutability of tuples by attempting to replace "DATA 6100" in elective_tuple with "DATA 7100" and observe the error or behavior.
# 6.	Modify the elective_tuple by converting it to a list, replacing "DATA 6100" with "DATA 7100", and then converting it back to a tuple.
# 7.	Determine whether the append() method can be used for tuples, explain why it cannot, and provide an alternative approach to add "DATA 9999" to core_tuple.
# 8.	Concatenate core_tuple, elective_tuple, and capstone_tuple to create a single tuple named DS_tuple and print the combined tuple.

core_tuple = ("DATA 5050", "DATA 5100", "COMP 5850", "COMP 6200")

elective_tuple = ("DATA 5200", "DATA 5300", "DATA 5400", "DATA 5500", "DATA 5900", "DATA 6100", "DATA 6150", "DATA 5350",
                 "COMP 5400", "COMP 5800", "COMP 6400", "COMP 6800")

capstone_tuple = tuple("DATA 6200")

print(core_tuple)
print(len(core_tuple))
print(core_tuple[0])
print(core_tuple[-1])
print()

print(elective_tuple)
print(len(elective_tuple))
print(elective_tuple[0])
print(elective_tuple[-1])
print()

print(capstone_tuple)
print(len(capstone_tuple))
print()

print(elective_tuple[1:3])
print()

check = "DATA 5400" in core_tuple
print(check)
print()

# elective_tuple[5] = "DATA 7100"
# print(elective_tuple)
# print()

elective_list = list(elective_tuple)
elective_list[5] = "DATA 7100"
elective_tuple = tuple(elective_list)
print(elective_tuple)
print()

#Append cannot be done to a tuple because a tuple is immutable. An alternate approach would be converting the tuple to a list,  appending the value "DATA 9999", and converting it back to a tuple.

DS_tuple = core_tuple + elective_tuple + capstone_tuple
print(DS_tuple)

#The problem with concatenating captone_tuple to DS_tuple is that it is a tuple with one value, so it makes each letter separate from eachother in the concatenation.