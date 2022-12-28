from asyncio import new_event_loop
from xml.dom.minidom import NamedNodeMap


a=34
b="neel"
c="bhimani"
print(a,b,c)
print(b+c)
print(type(a),type(b),type(c)) 
p=b+c
print(p)
d="the name is mahadev"
print(d)
name="neel"
print(name[1:3])
p=name[-3:-1]
print(p)
name="thegodisalmightygreat!"
print(name[1::4])
story=('mahadev is almighty god who is also known as bholenath')
t=(story[0:8])
print(t)
print(story[0:4])
#string functions
print(len(story))
print(story.endswith("djfjsfjhdsjg"))
print(story.count("a"))
print(story.capitalize())
print(story.find('''mahadev'''))
print(story.replace("mahadev","krishna"))
#escape sequence character
varta = '''my name \ni\'s\tNa\\me is neel'''
print(varta)

print(type(b))