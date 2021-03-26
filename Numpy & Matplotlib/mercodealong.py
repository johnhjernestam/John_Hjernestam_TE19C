import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-2,5)

def f(x):
    return -x**2+3*x+1

störst = np.max(f(x))
index = np.argmax(f(x))

print(x[index])

plt.plot(x,f(x))
plt.plot(x[index], störst, "r*")
plt.show() 
