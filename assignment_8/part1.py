import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(0, 4 * np.pi)


func1 = np.sin(x)
func2 = np.cos(2 * x)

plt.plot(x, func1, c = 'r', linewidth = '2')
plt.plot(x, func2, c = 'b', ls = '--', linewidth = '3')
plt.axis([0, 14, -2, 2])
plt.grid()
plt.title("multiple plots")
plt.xlabel("angle (radian)")
plt.ylabel("amplitude")
plt.legend(["sin", "cos"], loc="upper right")

plt.show()