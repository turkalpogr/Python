import  random

sayi = random.randint(1,10)


deneme = int(input("deneme yapamak istediğiniz miktarı girin: "))
count = 0
while deneme > 0:
    deneme -=1
    count += 1
    tahmin = int(input("lütfen sayı tahmininzi yazınız: "))
    if sayi == tahmin:
        print(f"tebrikler {count}.defada bildiniz {100 - (100 / deneme) * (count-1)}")
        break
    elif sayi > tahmin:
        print('yukarı')
    else:
        print('aşağı')
    if deneme == 0:
        print("deneme hakkınız bitti")

