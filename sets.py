fruits = {"orange","apple","banana"}
#listeler indexlenemez
print(fruits)



fruits.add("cherry")
#listelemelerde aynı elemanlar tekrardan eklenmek istense dahi yazdırma yaparken tekrarsızdır

fruits.remove('orange')
fruits.discard('banana')
for x in  fruits:
    print(x)
print(fruits)
