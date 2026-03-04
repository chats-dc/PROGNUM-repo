import numpy as np
func=input("Enter a function with symbols: ")
anum = input("Enter lower bound: ")
bnum = input("Enter upper bound: ")
a = float(anum)
b = float(bnum)
N = 1000000  #increased N will increase accuracy. i chose 1000000
x = np.linspace(a,b,N) #evenly spaced from a to b with N intervals
y = np.sum(eval(func))
integ = (b-a)/N*y
print(integ)