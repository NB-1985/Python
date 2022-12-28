from unicodedata import name


a="my  name is neel"
name=a.find("  ")
print(name)
name=a.replace("  "," ")
print(name)