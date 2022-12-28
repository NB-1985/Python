a={1,2,3,5,1}
print((type(a)))
print(a)    #set doesnot accept repeated value thats why we get  1 only one time in output
b={}
print(b)     
print(type(b)   )    #its not empty set it is dictionary as we can see in our output

#empty set can declare as shown below
c=set()  
print(c)
c.add(3)
c.add(9)
c.add((1,2,3,3,))
print(c)
print(type(c))
print(len(c))#gives length
c.remove(3)
print(c)
print(c.pop())#removes random element
c.clear()#clear the set and gives an empty set
print(c)