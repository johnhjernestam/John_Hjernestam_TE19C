import numpy as np 
import matplotlib.pyplot as plt

x = np.arange(1,10)

print(x)

def f(k,x,m):
    y = k*x + m
    return y

# y = 2x + 2
# print(f(2, x, 2))

# y = x + 1
#print(f"y = {f(1,x,1))}")
plt.plot(x,f(1,x,1))
plt.title("En rät linje")
plt.xlabel("x")
plt.ylabel("y")
plt.show() 
