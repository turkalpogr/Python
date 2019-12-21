name= "Mahmut Türkalp"

for a in name:
    if a == 't' or a =="T":
        continue
    print(a)


numbers = []

for x in range(11):
    numbers.append(x)

print(numbers)

numbers = [x for x in range(11)]
print(numbers)

numbers2 = [x*x for x in range(11) if x%3==0]
print(numbers2)

myStr = 'hello'
myLiat = []

for letter in myStr:
    myLiat.append(letter)
print(myLiat)

myLiat = [letter for letter in myStr]
print(myLiat)

years = [1976, 1966, 1995 , 1999 , 2003, 1970]
ages = [2019-year for year in years]
print(ages)
result = [x if x%2==0 else 'tek' for x in range(1,15)]
print(result)

sayilar = []

for x in range(1,7):
    for y in range(1,7):
        sayilar.append((x,y))
print(sayilar)
sayilar2 = [(x2,y2 )for x2 in range(1,7) for y2 in range(1,7)]
print(sayilar2)