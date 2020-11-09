import matplotlib.pyplot as plt

s = [0,10,20,30,40,50,60,70,80,90,100] #sträcka

t = [0, 1.83, 2.87, 3.78, 4.56, 5.5, 6.32, 7.14, 7.96, 8.79, 9.69] #tider

v = [0] #tom lista

for i in range(len(s)):
    v_i = ((s[i]-s[i-1])/(t[i]-t[i-1]))
    v.append(v_i)

plt.plot(t, s, '*r')
plt.show()
