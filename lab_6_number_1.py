import matplotlib.pyplot as plt

x = [1, 5, 5, 1, 1]
y = [1, 1, 5, 5, 1]

plt.plot(x, y, color='k', marker='o', ms=5)
plt.axis('square')

plt.savefig('fig_5.png')