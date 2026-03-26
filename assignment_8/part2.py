import matplotlib.pyplot as plt
import numpy as np

data = np.random.randint(0, 51, 1000)

plt.hist(data, 10, color = "yellow", edgecolor = "red", zorder = 3)
x = np.arange(0, 55, 5)
y = np.arange(0, 150, 10)
plt.xticks(x)
plt.yticks(y)
plt.axis([0, 50, 0, 140])
plt.grid(zorder = 0)
plt.title("Histogram of 1,000 random integers from 0 to 50")

plt.show()