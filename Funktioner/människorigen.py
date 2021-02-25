import numpy as np
import matplotlib.pyplot as plt

def N(t):
    return 11/(1+3.4*np.exp(-0.03*t))

print(f"Antal människor år 1950: {N(0)} miljarder")

år = 500

t = np.arange(år)
plt.plot(t, N(t))
plt.ylabel("Antal människor i miljarder")
plt.xlabel("År efter 1950")
plt.title("Modell för population")
plt.grid()

plt.show()
print(t)