#encoding : utf-8

#lamda = 0.2 E = 5

from scipy.stats import expon
import numpy as np
import matplotlib.pyplot as plt

rv = expon(scale = 5)

x = np.linspace(0.0, 30, 100)

print(rv.pdf(x))
plt.fill_between(x, rv.pdf(x), y2=0, color="coral", label="0.2")
plt.axvline(x = rv.mean(), label="E(X)", linewidth=1.5, color="blue")
plt.grid(True)
plt.legend()

plt.xlim([0, 25])
plt.ylim([0, 0.2])
plt.title("exponential distribution")
plt.xlabel("RV")
plt.ylabel("f(x)")

plt.show()