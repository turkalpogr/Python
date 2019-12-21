numbers = [1,2,3,4,5]

#1 den 100e kadar sayıları yazdırma
"""x =0
while x<100:

    print(x)
    x += 1
"""
#*****************************************
"""name = ''
while not name.strip():
    name = input('Lütfen adınızı giriniz: ')

print(name)
"""
#*****************************************
"""
sayilar = [1,3,5,7,9,12,19,21]
count = 0
while count < len(sayilar):
    print(sayilar[count])
    count +=1

#**************************************

sayi = int(input('Lütfen başlangıç değerini girinniz: '))
sayi2 = int(input('lütfen bitiş değerini yazınız: '))

while sayi < sayi2:
    if sayi%2==1:
        print(sayi)
    sayi +=1
#*********************************************
x = 100
while  x>0:
    print(x)
    x-=1
#*******************************************
i = 0
dizi = []
while i<5:
    girdi = int(input("girilecek olan sayıları giriniz"))
    dizi.append(girdi)
    i += 1
dizi.sort()
print(dizi)"""

urunler = []

adet = int(input("Kaç adet ürün girmek istiyordunuz "))
i = 0
while i< adet:
    name = input("ürün adı")
    price = input("fiyat")
    # append ile dizilere ekleme yapılır
    #dizi içinde liste kullanarak dictionary tipi listeleme yapılmış olur
    urunler.append(
        {
            'name' : name,
            'price' : price
        }
    )
    i += 1
for a in urunler:
    print(f"ürün adı {a['name']} fiyatı {a['price']}")

