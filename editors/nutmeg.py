#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

print("This file was created using the nano editor by Aaron W")

# Generate some random Gaussian noise

x = np.random.randn(10)
y = np.random.randn(10)

fig, ax = plt.subplots(1)

ax.scatter(x, y)

plt.show()

