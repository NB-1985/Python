'''a=4
if(a>5):
    print("the value is greater than 5")
    if(a<99):
        print("the value is")
elif(a>6):
    print("the value is greater than 6")
else:
    print("the value is not greater than 5 or 6")
print("done")
b=3
if(b>5):
    print("greater")
else:
    print("lessser")'''

    #age vado programe

'''a=input("enter your age\n")
a=int(a)
if (a>=18):
    print("Yes")   #relational operators
else:
    print("no")'''

#logical operators

age=input("enter your age\n")
age=int(age)
 
if (age>=18 and age<=50):    #instead of and we can use or,not
    print("you can work with us")
else:
    print("you are not work with us")


b=None
if (b is None):
    print('yes')
else:
    print("no")



k=[2,3,4,"6",
] 
print('6' in k)