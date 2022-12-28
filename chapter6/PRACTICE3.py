'''text=input("enter a text\n")
if("make a lot of money"in text):
    print("it is spam")
elif("subscribe this"in text):  #if pan use kari sakay
    print("this is spam")
if("buy now" in text):
    print("this is spam")
else:
    print("this is not spam")
print("done")'''



text=input("enter a text\n")
if("make a lot of money"in text  or "buy now"in text or " subscrube this" in text):
    print("it is spam")
else:
    print("this is not spam")
