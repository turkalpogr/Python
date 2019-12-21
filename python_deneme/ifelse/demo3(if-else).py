import datetime
tarih = input(" aracınızın trafiğe çıkış tarihini aralarına / koyarak yıl ay gün şeklinde yazınız ")
tarih = tarih.split('/')

yil = datetime.datetime(int(tarih[0]),int(tarih[1]),int(tarih[2]))
simdi = datetime.datetime.now()
fark = simdi - yil
dayss = fark.days
if (dayss<=365):
    print("aracınızın 1. bakımı")
elif (dayss>365) and dayss<=365*2:
    print("aracınızın 2. bakımı")
elif (dayss>365*2) and dayss<365*3:
    print("aracınızın 3. bakımı")