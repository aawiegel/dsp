#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

print("This file was created in emacs by Aaron W.")

# Create exponential noise and plot

x = np.random.exponential(size = 10)
y = np.random.exponential(size = 10)

fig, ax = plt.subplots(1)

ax.scatter(x, y)

plt.show()
