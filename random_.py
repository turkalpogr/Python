import random
#random metodu bu şekilde çağırırsak random.... şeklinde kullanmak icapeder

result = dir(random)
print(result)
result = random.random()*100
print(result)
result = int(random.uniform(1,15))
print(result)
#dönen random değerini int yapmaktansa bu hazır method kullanmaya daha el  verişlidir
result = random.randint(1,100)
print(result)
names = ['aliş','mahmut','musa','deneme','musa','ayten','melike']
result = names[random.randint(0,len(names)-1)]
print(result)
#bir dizi çalıştırırken bu fonksiyon ile dizi içinden bir aralık belirtmeden de random olarak değer almak mümkündür
result = random.choice(names)
print(result)
#choies metodu ile liste yada string bir değerin içinden rastgele öğe çağırabiliriz
greeting = " Mahmut Türkalp"
result = random.choice(greeting)
print(result)
#shuffle ile liste elemanları karıştırılmış bir şekilde karşımıza gelir
liste = list(range(10))
random.shuffle(liste)
print(liste)
#sample ile liste, string, dizi gibi öğelerin içinden belirtilen sayıda rastgele eleman seçme imkanımız olur
liste = list(range(20))
result = random.sample(liste,3)
print(result)
