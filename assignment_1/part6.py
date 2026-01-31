# Write a Python program that performs the following tasks:
# 1.	Create three dictionaries: core_dictionary, elective_dictionary, and capstone_dictionary where the keys are course numbers (e.g., "DATA 5050") and the values are course titles (e.g., "Programming for Data Science").
# 2.	Print the contents of each dictionary.
# 3.	Print the keys of each dictionary.
# 4.	Print the value that corresponds to the key "DATA 6200" in capstone_dictionary.
# 5.	Add a new element to elective_dictionary with the key "DATA 6500" and the value "Unknown Course". Print elective_dictionary after adding the new element.
# 6.	Add a repeated element to core_dictionary with the key "DATA 5100" and the value "Programming for Data Science". What do you observe? Explain the behavior.
# 7.	Remove a specific element with the key "DATA 5300" from elective_dictionary using the pop() method. Print the removed element and the updated dictionary.

core_dictionary = {"DATA 5050": "Mathematics for Data Science", "DATA 5100": "Programming for Data Science", "COMP 5850": "Data Visualization", "COMP 6200": "Machine Learning"}

elective_dictionary = {"DATA 5200": "Statistical Learning", "DATA 5300": "Data Mining", "DATA 5400": "Algorithms for Data Science", "DATA 5500": "Business Analytics",
                        "DATA 5900": "Special Topics", "DATA 6100": "Natural Language Processing", "DATA 6150": "Applied Deep Learning", "DATA 5350": "Applied Statistics for Data Science", "COMP 5400": "Hybrid and Relational Databases", "COMP 5800": "Introduction to Bioinformatics", "COMP 6400": "Dis. Algorithms Design and Data Analysis", "COMP 6800": "Introduction to Computer Vision"}

capstone_dictionary = {"DATA 6200": "Data Science Capstone"}

print(core_dictionary)
print(core_dictionary.keys())
print()

print(elective_dictionary)
print(elective_dictionary.keys())
print()

print(capstone_dictionary)
print(capstone_dictionary.keys())
print()

print(capstone_dictionary["DATA 6200"])
print()

elective_dictionary["DATA 6500"] = "Unknown Course"
print(elective_dictionary)
print()

core_dictionary["DATA 5100"] = "Programming for Data Science"
print(core_dictionary)
print()
#I observe that after adding a repeated element to core_dictionary, there is still only one element that reads "DATA 5100": "Programming for Data Science". This is because dictionaries do not allow duplicate elements.

removed_element = elective_dictionary.pop("DATA 5300")
print(removed_element)
print()
print(elective_dictionary)