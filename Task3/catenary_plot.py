from matplotlib import pyplot as plt
import numpy as np
x = []
y=[]
a=-5
for a in range(-5,6):
    x.append(a)
    b=((np.exp(a)+np.exp(-a))/2)
    y.append(b)

plt.plot(x,y,marker=".",color="black",label="$\cosh(x)$")
plt.title("cosh function",color="red")
plt.xlabel("x value", fontsize=14, color="grey")
plt.ylabel("function", fontsize=14, color="grey")
plt.grid()
plt.xlim(-5,6)
plt.legend()
plt.show()

h = np.arange(x[0],max(x)+1)

print(h)
