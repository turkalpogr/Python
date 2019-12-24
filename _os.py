import os
"""os ile beraber işletim sisitemi özellikleri kullanılabilir
"""
result = dir(os) # içerikte kullanılabilecek modülleri yazdırır
result = os.name #işletim sisteminin adını yazar
#os.chdir() bu element ile beraber dosya dizini değiştirielebilir
#ayrıyetten dizin değiştirmek içinde kullanılabilir
result = os.getcwd() #bulunulan dizini yazdırır
#dosya klasör oluşturma
#os.mkdir("new_dr")
# çoklu veya içiçe dosya oluşturmak için kullanılır
#os.makedirs("new_dr/yeni")
#içinde bulunulan dizndeki dosyaları yazdırır
#eğer parantez içinde bir konum belirtilirse o konumda olan dosya ve klasörleri yazdırır
result = os.listdir()
#bu işlem ile beraber herhangi bir filtreleme ve listeleme yapılabilir
"""for dosya in result:
    if dosya.endswith(".py"):
        print(dosya)"""
#herhangi bir dosyanın hakkındaki bilgileri yazdırabiliriz
#result = os.stat("argument.py")

print(result)
