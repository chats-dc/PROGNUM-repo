n = 0
num1 = 0
num2 = 1
fibo=0
for n in range(100):
    if n<2:
        fibo=fibo+num2
    else:
        fibo=num1+num2
    num1=num2
    num2=fibo
    n+=1

print(fibo)
        
    
    