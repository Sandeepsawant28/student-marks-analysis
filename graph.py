import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([1, 2, 6, 11])
ypoints = np.array([3, 8, 1, 11])

plt.plot(xpoints, ypoints)
plt.xlabel("X-axis Label")
plt.ylabel("Y-axis Label")
plt.title("My first graph!")
plt.show() # Required to display the plot in a script
