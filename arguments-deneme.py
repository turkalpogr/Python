"""
kelime = input('Lütfen tekrarlanması gerekn kelimeyi giriniz')
kez = int(input('tekrar sayını giriniz'))

def tekrar(x,y):
    for a in range(0,y):
        print(x)

tekrar(kelime,kez)

#******************************************
print("********************************************")

liste2 =[]
def liste(*args):

    for x in args:
      liste2.append(x)
    return (liste2)

print(liste(10,20,30,40,50,"merhaba"))

print("**********************************************")

def asalch(say, say2):
    for sayii in range(say, say2+1):
        if sayii > 1 :
            for i in range(2,sayii):
                if sayii%i==0:
                    break
            else:
                print(sayii)

sayi1 = int(input())
sayi2 = int(input())
asalch(sayi1,sayi2)
"""
def tambolen(x):
    liste = []
    for y in range(1,x+1):
        if x%y ==0:
            liste.append(y)
    return liste
say = int(input())
print(tambolen(say))

print("*************************************")
def tambolen2(x):

    for y in range(1,x+1):
        if x%y ==0:
            print(y)

say = int(input())
print(tambolen2(say))