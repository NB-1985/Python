from pickle import TRUE


a=[4,5,6,7,89,10,7,1]
a[-1]=98
print(a[-4])
print(a)
g=['neel','bhimani','har har mahadev',46,False,True,6.6]
print(type(g))
print(g)
print(g[0:3]) #list slicing
g.append(55)#append() operetor adds what you type at the end of list
print(g)
a.sort()#chadata kram ma githve sort()
print(a)
a.reverse()#utarta kram ma gothve reverse()operator
print(a)
a.insert(6,8)#this will add 8 at 6th index
print(a)
g.pop(2)#delete element at index 2
print(g)
g.remove(46)#removes what you type but its present in list its compolsary 
print(g)