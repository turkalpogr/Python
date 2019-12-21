from builtins import int

deneme = {}

sayi = input('öğrenci numaranızı giriniz ')
ad = input("Adınızı giriniz: ")
sad = input("soyadınızı giriniz: ")
telefon = input("telefon numaranızı giriniz: ")

deneme.update({
    sayi : {
        'ad': ad,
        'soyad': sad,
        'telefon': telefon
    }
})
print(deneme)


