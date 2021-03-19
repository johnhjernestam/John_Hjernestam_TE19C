import numpy as np 
import matplotlib.pyplot as plt

x = np.arange(0,11)

def f(k,x,m):
    y = k*x + m
    return y

y = 3*x + 1
print(f(3, x, 1))

plt.plot(x,f(3,x,1))
plt.title("En rät linje")
plt.xlabel("x")
plt.ylabel("y")
plt.show()