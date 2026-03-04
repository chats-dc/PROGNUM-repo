aval = input('Enter a value for a: ')
bval = input('Enter a value for b: ')
cval = input('Enter a value for c: ')

a=float(aval)
b=float(bval)
c=float(cval)

D=b**2 - 4*a*c
if D == 0:
    sol=(-b/(2*a))
    print(f'x = {sol} is the only solution')
elif D>0: 
    sol1= (-b+D**0.5)/(2*a)
    sol2 = (-b-D**0.5)/(2*a)
    print(f'The two solutions are: {sol1} and {sol2}')

else: 
    print('There are no solutions to this.')
    