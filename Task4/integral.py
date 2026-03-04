import scipy.integrate as integ

func=input("Enter a function with symbols: ")
anum = input("Enter lower bound: ")
bnum = input("Enter upper bound: ")
a = float(anum)
b = float(bnum)


from sympy import *
init_printing(use_unicode=False)
x = Symbol('x')
answer = integrate(func, (x,a,b))

print(f"The definite integral is: {answer}")
