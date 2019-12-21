"""sayilar = [1,3,5,7,9,12,19,21]

count = 0

for x in sayilar:
    if x%3==0 :
        count +=1
    print(x)

print(count)

toplam = 0
for a in sayilar:
    toplam += a
print(toplam)

for b in sayilar:
    if(b % 2 ==1):
        print(b**2)"""

#*******************************************************************************

"""
cities = ["kocaeli","istanbul", "ankara", "izmir", "rize"]

for city in cities:
    if(len(city) > 5):
        print(city)

"""
#*******************************************************************************

product = [
    {'name': 'Samsung S6', 'price': ' 3000'},
    {'name': 'Samsung S7', 'price': ' 4000'},
    {'name': 'Samsung S8', 'price': ' 5000'},
    {'name': 'Samsung S9', 'price': ' 6000'},
    {'name': 'Samsung S10', 'price': ' 7000'}
]
toplam = 0

for p in product:
    toplam += int(p['price'])

print(toplam)

for p in product:
    if int(p['price']) < 5000:
        print(p['name'])
