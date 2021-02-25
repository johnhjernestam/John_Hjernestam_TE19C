import matplotlib.pyplot as plt

y = [2*x-2 for x in range(10)]
x = [x for x in range(10)]
print(f"x: {x}")
print(f"y: {y}")

plt.plot(x,y)
plt.xlabel("x")
plt.ylabel("y")
plt.show()