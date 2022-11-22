import matplotlib.pyplot as plt
import numpy as np

x = np.array([0,10])
y = np.array([0,250])
plt.plot(x,y, marker = 'o', linestyle = 'dashed', color = 'red')
plt.show()

ypoint = np.array([10,5,3,9,3])

plt.plot(ypoint, marker = '*')
plt.show()

x = np.array(["A","B","C","D"])
y = np.array([5,8,6,3])

plt.bar(x,y)
plt.show()