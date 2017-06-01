#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

print("This file was created in vim by Aaron W")

# Pull random numbers from a uniform distribution and plot

x = np.random.random(10)
y = np.random.random(10)

fig, ax = plt.subplots(1)

ax.scatter(x, y)

plt.show()
