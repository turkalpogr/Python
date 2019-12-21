# _*_ coding:utf8 _*_
#key value mantığı vardır
sehirler = ["Erzincan","Malatya"]
plaka = [24,44]

# print(plaka[sehirler.index("Erzincan")])
# yani yukarıdaki mantığın şu şekilde çalışması lazımdı
# print(plaka["Erzincan"]) => 24 olması gerekirdi

plakalar = {"Erzincan" : 24 , "Malatya" : 44}

# print(plakalar["Erzincan"])
# #dictionary listeleri üzerine eklme yaparken 
# plakalar["Elazığ"] = 23
# print(plakalar)

# #value değeri üzerinde değişiklik yapğarken 
# plakalar["Erzincan"] = 'Eğin'
# print(plakalar)

ogrenciler = {}

number = input("numranızı giriniz")
ad = input("adınızı giriniz")
sad = input("syadınızı giriniz")
telefon = input("telefon numaranızı giriniz")

ogrenciler.update({
   number : {
       'Adı' : ad,
       'Soyadı' : sad,
       'Telefonu' : telefon
   }
})


