# Write a Python program that performs the following tasks:
# 1.	Create three lists: core_list, elective_list, and capstone_list, containing course numbers as strings (e.g., "DATA 5050").
# 2.	Print the contents of each list, the number of courses in each list using the len() method, and the first and last courses in each list using indexing.
# 3.	Display the second and third elective courses using slicing.
# 4.	Check if "DATA 5400" is in core_list using the in operator and print True or False.
# 5.	Demonstrate that lists are mutable by replacing "DATA 6100" in elective_list with "DATA 7100" using appropriate index and then appending "DATA 9999" to core_list.
# 6.	Concatenate core_list, elective_list, and capstone_list to create a single list named DS_list and print the combined list.

core_list = ["DATA 5050", "DATA 5100", "COMP 5850", "COMP 6200"]

elective_list = ["DATA 5200", "DATA 5300", "DATA 5400", "DATA 5500", "DATA 5900", "DATA 6100", "DATA 6150", "DATA 5350",
                 "COMP 5400", "COMP 5800", "COMP 6400", "COMP 6800"]

capstone_list = ["DATA 6200"]

print(core_list)
print(len(core_list))
print(core_list[0])
print(core_list[-1])
print()

print(elective_list)
print(len(elective_list))
print(elective_list[0])
print(elective_list[-1])
print()

print(capstone_list)
print(len(capstone_list))
print(capstone_list[0])
print(capstone_list[-1])
print()

print(elective_list[1:3])
print()

check = "DATA 5400" in core_list
print(check)
print()

elective_list[5] = "DATA 7100"
print(elective_list)
print()

core_list.append("DATA 9999")
print(core_list)
print()

DS_list = core_list + elective_list + capstone_list
print(DS_list)