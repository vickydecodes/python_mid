#matplotlib and numpy


import matplotlib.pyplot as plt
import numpy as np

x = np.random.normal(10, 250, 170)

plt.hist(x, color='red')

plt.show()