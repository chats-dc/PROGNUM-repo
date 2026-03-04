import math

year = input('Please enter a year: ')
Y = float(year)

month = input('Please enter a month: ')
M = float(month)

day = input('Please enter a date: ')
D = float(day)

#math.floor() is used for the whole integer. Every quotient gets a math.floor() 
#had to search it up. found it on www.tradingcode.net
JD = 367*Y -7*math.floor((Y+math.floor((M+9)/12))/4) \
-3*math.floor((math.floor(math.floor((Y+(M-9)/7))/100) + 1)/4) + \
math.floor((275*M)/9) + D + 1721029-0.5



print(f'The Julian Date is: {JD:15.2f}')