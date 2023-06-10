import matplotlib.pyplot as plt

plt.plot([1, 2, 3, 4], [5,7,9,11], label='Price ($)')
plt.plot([1, 2, 3, 4], [3, 5, 9, 7], label='Demand (#)')
plt.xlabel('X-label')
plt.ylabel('Y-label')

plt.legend(loc='best',ncol=2)

plt.show()