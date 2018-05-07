#encoding : utf-8


from scipy.stats import norm
import numpy as np
import matplotlib.pyplot as plt


rv = norm(0, 1)
x = np.linspace(-5, 5, 200)


plt.fill_between(x, rv.pdf(x), y2=0.0, color="coral", label="N(0,1)")
plt.axvline(x = rv.mean(), label="E(X)", linewidth=1.5, color="blue")
plt.legend()
plt.grid(True)

plt.xlim([-5, 5])
plt.ylim([-0.0, 0.5])

plt.title("normal distribution")
plt.xlabel("RV")
plt.ylabel("f(x)")

plt.show()