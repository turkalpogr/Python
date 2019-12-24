import re

result = dir(re)

#regular expression
# re module
#temel amaç arama filtreleme
str = "Deneme amaçlı yazı| lalalalla"
#re.findall()
result = re.findall("yazı", str)
result = len(re.findall("yazı", str))
result = re.split(" ",str)
#re.sub()
result = re.sub("\s", "-",str)
#re.search()
result = re.search("amaç",str)
result = result.start()
print(result)