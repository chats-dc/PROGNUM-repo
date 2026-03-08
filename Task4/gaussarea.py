## executable script with inputs:
import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate

def gauss(x, A, x0, sigma, z0):
    return A*np.exp(-(x-x0)**2/(2*sigma**2))+z0
A_val = input('Please enter a coefficient (A):')
x0_val = input('Please enter x0:')
sig_val= input('Please enter sigma:')
z0_val = input('Please enter z0:')
a_val = input('Please enter the lower bound:')
b_val = input('Please enter an upper bound:')
A = float(A_val)
x0 = float(x0_val)
sig = float(sig_val)
z0 = float(z0_val)
a = float(a_val)
b = float(b_val)

x=np.linspace(-10,10,200) #numbers from -10 t0 10 with 200 spaces between
gaussian = gauss(x,A,x0,sig,z0) #uses gauss function for the x values
integral = integrate.quad(gauss, a, b,args = (A, x0, sig, z0))
#arguments were needed for gauss function because quad works with functions; not lists


integralinf = integrate.quad(gauss, -np.inf, np.inf,args = (A, x0, sig, z0))

print(f'The integral within the limits is:{integral[0]}')
print(f'The infinite integral is: {integralinf[0]}')
plt.fill_between(x, gaussian, where=(x >= a) & (x <= b), \
                 color='blue',alpha=0.5,label = f'Area={integral[0]:.2f}')
plt.plot(x,gaussian,label = 'gaussian')
plt.legend()
plt.show()