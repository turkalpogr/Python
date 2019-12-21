# _*_ coding: utf8 _*_
'''
Kullanıcıdan daire yarı çapı değer alınarak yapılacak olan program yaz
'''
pi = 3.14
yariCap = input("Yarı çap değeri giriniz")
alan = pi*(yariCap**2)
cevre = pi * 2 * yariCap
print("Alanınız: "+str(alan)+" "+"Alanınız: "+str(cevre))