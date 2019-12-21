#uygulama

x , y , z = 2 , 5 , 107
numbers = 1, 5 , 7 ,10 ,6

sayi = int( input('ilk sayıyı giriniz'))
sayi2 = int( input('ikinci sayıyı giriniz'))

sayi *= sayi2

toplam = x+y+z


print(sayi-toplam)
print(y//x)
print(toplam%3)
print(y**x)
x ,*y,z = numbers
print(z**3)
print(y[0] + y[1] + y[2])