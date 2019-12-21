sayi = int(input("kontrol için bir sayı giriniz: "))

count = 0


for a in range(2,sayi):

    if sayi%a==0:
        count +=1
        break
    a += 1
if count !=0:
    print("sayı asal değildir")
else:
    print("sayınız asaldır")