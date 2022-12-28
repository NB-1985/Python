from typing import Tuple


mydict={
         "name":'neel is good boy',
         "dict":{'neel':1},
         '''marks''':[1,2,3]
        }
print(mydict) 
print(type(mydict))
print(mydict["marks"])
print(type("marks"))
mydict["marks"]=[45,78,0]
print(mydict)
print(mydict['dict']["neel"])
print(mydict.keys())




############################################DICTIONARY METHODS#############################

print(list(mydict.keys())) #print keys of dictionary
print(mydict.values()) #'print the value of dictionary
print(mydict.items())#PRINT THE KEY,VALUE for ALL CONTENT OF DICTIONARY
updatedict={
    'neel':"good boy"

}
mydict.update(updatedict)
print(mydict)
print(mydict.get("neel"))