sinav = float(input("Lütfen ilk sınavdan aldığnız notu giriniz"))
sinav2 = float(input("Lütfen ikinci sınavdan aldığınız notu giriniz"))
ortalama = (sinav+sinav2)/2

if ortalama >=0 and ortalama <=24:
    print(f"Birinci sınavdan aldığpınız puan {sinav} ve ikinci sınavdan aldığınız puan { sinav2} "
          f"ortalamanız ise {ortalama}, bu sınavdan aldığınız puan = 0")
elif ortalama >= 25 and ortalama <= 44 :
    print(f"Birinci sınavdan aldığpınız puan {sinav} ve ikinci sınavdan aldığınız puan {sinav2} "
          f"ortalamanız ise {ortalama}, bu sınavdan aldığınız puan = 1")
elif ortalama >=45 and ortalama <=54:
    print(f"Birinci sınavdan aldığpınız puan {sinav} ve ikinci sınavdan aldığınız puan {sinav2} "
          f"ortalamanız ise {ortalama}, bu sınavdan aldığınız puan = 2")
elif ortalama >= 54 and ortalama <=69:
    print(f"Birinci sınavdan aldığpınız puan {sinav} ve ikinci sınavdan aldığınız puan {sinav2} "
          f"ortalamanız ise {ortalama} bu sınavdan aldığınız puan = 3")
elif ortalama >= 70 and ortalama <= 84:
    print(f"Birinci sınavdan aldığpınız puan {sinav} ve ikinci sınavdan aldığınız puan {sinav2} "
          f"ortalamanız ise {ortalama} bu sınavdan aldığınız puan = 4")
elif ortalama >=85 and ortalama <=100:
    print(f"Birinci sınavdan aldığpınız puan {sinav} ve ikinci sınavdan aldığınız puan {sinav2} "
          f"ortalamanız ise {ortalama} bu sınavdan aldığınız puan = 5")

else:
    print("Notunuz hesaplanamadı")