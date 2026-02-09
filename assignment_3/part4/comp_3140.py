# In this part of the assignment, you will create a Python module named comp_3140_utilities.py that contains multiple functions related to student data processing.

# Part-4(a) (15 Points): Create a module named comp_3140_utilities.py that includes the following functions. Each function takes a list of scores.
# •	average_score(scores), returns the average score.
# •	highest_score(scores), returns the highest score.
# •	lowest_score(scores), returns the lowest score.
# •	score_range(scores), returns the range (difference between the highest and lowest scores).

# Part-4(b) (15 Points): In a separate file named comp_3140.py, write a program that:
# •	Prompts the user to enter scores separated by spaces.
# •	Converts the input to a list of floats.
# •	Imports the functions from the comp_3140_utilities.py module.
# •	Calls each function and displays the results.

from comp_3140_utilities import average_score, highest_score, lowest_score, score_range

prompt = input("Enter scores separated by spaces: ")
scores = [float(s) for s in prompt.split()]

print(f"Average: {average_score(scores)}")
print(f"Highest: {highest_score(scores)}")
print(f"Lowest: {lowest_score(scores)}")
print(f"Difference: {score_range(scores)}")