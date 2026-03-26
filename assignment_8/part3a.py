import matplotlib.pyplot as plt
import numpy as np

students = ['Chris', 'John', 'Amber', 'Cassandra', 'David']
assignment1 = [55, 72, 91, 67, 98]
assignment2 = [81, 85, 92, 75, 95]

plt.bar(students, assignment1, color = 'pink')
plt.ylabel("Scores")
plt.xlabel("Students")
plt.title("Assignment 1 Scores")

plt.show()