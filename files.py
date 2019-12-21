"""file = open("newfile.txt", "w")
file.close()
file = open(fileSRC,"w")
print(file)
file.close()""""""
fileSRC = "/home/turkalp/Masaüstü/deneme/deneme.txt"
#file open a eklenebilecek üçüncü bir attribute ile bereaber encoding yazarak dil paketide belirlenebilir
#mevcutta dosya varsa içeriği silip üzerine yazar
file = open(fileSRC, "w")
file.write("Mahmut Türkalp")
file.close()
print(file)"""
#a modundaki mantık append ile eşdeğerdir
#üstüne ekleme yapar
fileSRC = "/home/turkalp/Masaüstü/deneme/deneme.txt"
file = open(fileSRC, "a")
file.write("Mahgmut TÜRKALP")
file.close()