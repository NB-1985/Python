letter=''' dear<|NAME|>,
GREETINGS OF THE DAY
you are selected
date:<|date|>
HAR HAR MAHADEV

'''
name=input("enter your name\n") 
date=input("enter date\n")
letter=letter.replace('''<|NAME|>''',name)
letter=letter.replace('<|date|>',date)
print(letter)