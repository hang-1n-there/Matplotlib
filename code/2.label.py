import matplotlib.pyplot as plt
import numpy as np

x = np.array([1,2,3,4])
y = np.array([3,5,9,14])
plt.plot(x,y)

plt.xlabel('X-label')
plt.ylabel('Y-label')

plt.show()