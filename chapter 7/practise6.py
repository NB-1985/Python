#factorial
from math import factorial


num =int(input("enter a number\n"))
n=1
for i in range(1,num+1):
    f=n*i
print("the factorial of number is",f)