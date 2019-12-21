
"""
notlari_gir ile kullanıcıya bazı sorular soruldu ve bu sorularla değerler alındu
bu değerleri işlemek için file işlemleri kullanıldı,

"""
def ortalama_gir():
    ad = input("Adını gir")
    adsoy = input("Adını gir")
    notu = input("Adını gir")
    notu2 = input("Adını gir")
    notu3 = input("Adını gir")

    with open("Sinav_notu.txt","a") as file:
        file.write(ad+" "+adsoy+" : "+notu+","+notu2+","+notu3+"\n")


def ortalama_oku():
    with open("Sinav_notu.txt","r") as file:
       for satir in file:
           print(notlari(satir))
def notlari(satir):
    satir = satir[:-1]
    liste = satir.split(':')
    ogrenci = liste[0]
    notlar = liste[1].split(',')
    not1 = int(notlar[0])
    not2 = int(notlar[1])
    not3 = int(notlar[2])
    ortalama = (not1 + not2 + not3)/3
    harf = ''
    if ortalama > 90:
        harf = 'AA'
    elif ortalama >= 80:
        harf = 'Ba'
    elif ortalama >= 65:
        harf = 'CC'

    return ogrenci + ': '+ harf+ '\n'

def notlarikayit():
    with open("Sinav_notu.txt", "r") as file:
        liste = []
        for i in file:
            liste.append(notlari(i))
        with open("sonuc.txt", "w") as file2:
            for i in liste:
                file2.write(i)

while True:
    islem = input("!- Notları oku"
                  "2- Not gir"
                  "3- Notları kaydet")
    if islem == '1':
        ortalama_oku()
    elif islem == '2':
        ortalama_gir()
    elif islem == '3':
        notlarikayit()
    else:
        print("Yaptığınız işlemleri tekrar kontrol ediniz")
        break

