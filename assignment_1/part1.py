#Write a Python program that asks the user to enter their name, major, student ID, and year of study (Freshman, Sophomore, Junior, Senior, Master, PhD), then displays a welcome message using three string formatting methods: classical (%), format() method, and f-string. After reviewing the “History of Programming Languages” lecture notes, include a unique fun fact related to a specific programming language or historical figure. The fun fact must be different for each student and must come directly from the lecture notes.

name = input("Enter your name: ")
major = input("Enter your major: ")
student_id = input("Enter your ID: ")
year_of_study = input("Enter your year of study: ")

print()

print("Displaying message classic way: ")
print("Welcome to TSU %s, %s %s with ID %s." % (major, year_of_study, name, student_id))

print()

print("Displaying message using string format method: ")
print("Welcome to TSU {}, {} {} with ID {}.".format(major, year_of_study, name, student_id))

print()

print("Displaying message using f-string: ")
print(f"Welcome to TSU {major}, {year_of_study} {name} with ID {student_id}.")

print()

print("Displaying a fun fact from the lecture notes: ")
print("Top 10 finance institutions use COBOL for their enterprise computing systems language.")