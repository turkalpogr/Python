#_*_ coding: utf8 _*_
message = " Hello there. My name is Mahmut Türkalp"

# message = message.upper() yazıları büyük yazdırmak için
# message = message.lower() yazıları küçük yazdırmak için
# message = message.title() bütün kelimelerin baş harfleri büyük yazılır
# message = message.capitalize() sadece baştaki harf büyük yazılır
# message = message.strip() baştaki ve sondaki boşlukları silmek için kullanılır
# message = message.split() regex olarak parantez içine göre stringi parçalama yapar
# message = message.split('.')
# print(message[1])
# message = message.split()
# print(message)
# message = '*'.join(message) #join ile ekleme yapar 
# # aynı zamanda birleştirme yaparkende join fonksiyonu kullanılır
# index = message.find('Mahmut') # ile cümle içinde parantezin içindeki kelimeye göre arama yapılır ve bu arama sonucunda indis numarası yazdırılır
# #başlama indisi yazdırılır
# print(index)
# print(message)
# isFound = message.startswith('H')
# print(isFound)
# isFoundEnd = message.endswith("p")
# print(isFoundEnd)
# message = message.replace('Mahmut','Mustafa')
# print(message)
#bu method ile yazdığımız yazıyı ortalam yaparken kullanılır
message = message.center(100,'*')
print(message)


