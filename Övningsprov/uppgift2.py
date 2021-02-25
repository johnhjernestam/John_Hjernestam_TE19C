import matplotlib.pyplot as plt 

def f(x):
    return x**2-3*x+1

x = [i for i in range(10)]
y = [f(i) for i in x]

plt.plot(x, y)
plt.xlabel("x")
plt.ylabel("y")
plt.show()
