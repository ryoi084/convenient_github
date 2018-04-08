import numpy as np
import matplotlib.pyplot as plt

def func(x, a, b, c, d):
    return a*x**3 + b*x**2 + c*x + d

x = np.linspace(-10, 10, 100)

fig = plt.figure()

plt.plot(x, func(x, 2.0, 5.0, -3.0, 2.0))

plt.show()
