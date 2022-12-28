#prime or n
num=input("enter a number:\n")
num=int(num)
prime= False
for i in range (2,num):
    if(num%i==0):
        prime= True 
        break
if prime:
    print("this number is not prime")
else:
    print("prime")