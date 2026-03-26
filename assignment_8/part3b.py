import matplotlib.pyplot as plt
import numpy as np

students = ['Chris', 'John', 'Amber', 'Cassandra', 'David']
assignment1 = [55, 72, 91, 67, 98]
assignment2 = [81, 85, 92, 75, 95]


plt.plot(students, assignment1, c = 'b', marker = 'o', zorder = 3)
plt.plot(students, assignment2, c = 'r', marker = 's', zorder = 3)
plt.ylabel("Scores")
plt.xlabel("Students")
plt.title("Assignment Scores Comparison")
plt.legend(["Assignment 1", "Assignment 2"], loc="upper right")

plt.grid(zorder = 0)
plt.show()