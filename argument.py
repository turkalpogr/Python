def changename(n):
    n = 'ada'

name = 'yiğit'
changename(name)
print(name)

#bu durumda python daki fonksiyonlar aslında çok interaktif şekilde çalışıyor diğer dillere nazaran daha az bir şekilde durum değişiklikleri yapmak mümkün
#buradaki esas mantık adres kopyalama yapmaktır

def change(x):
    x[0] = 'deneme'

sehir = ['s','k']

change(sehir)

print(sehir)
# silicing işlemi ile bütün bir diziyi farklı bir adres üzerinde kopyalama yapabiliriz




def add2(x,y):
    return sum((x,y))
print(add2(10,20))

def add(*params):
   sum = 0
   for x in params:
       sum = sum + x
   return sum
print(add(10,20,30,40,50,100))

# tek yıldız ile tuple liste yollayabiliriz
# ** ile dictionary tipi liste gönderebiliriz java daki adıyla set listler
def setlist(**args):
    for key,value in args.items():
        print("{} {}".format(key,value))

setlist(name = 'mahmut',age = 24, email='turkalp24@gmail.com')

# bu şekilde mix bir lekilde kullanımda mümkün

def Func(a,b,*args,**kwargs):
    print(a)
    print(b)
    print(args)
    for key , value in kwargs.items():
         print(f"{key} ve {value}" )

Func(10,20,30,40,50,60,70,deneme = 'bu ne mk', ne = 'ne diyon la sen ')
