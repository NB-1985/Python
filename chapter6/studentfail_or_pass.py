a=int(input("enter first sub marks\n"))
b=int(input("enter second sub marks\n"))
c=int(input("enter third sub marks\n"))

if (a<33 or b<33 or c<33):
    print("you are fail due to less than 33 marks")
elif(a+b+c)/3 <40:   #if pan use kari sakay
    print("you are fail due to less than 40 percentage")
else:
        print("you are pass")
