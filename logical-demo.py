#1
sayi = int(input('Kontrol için bir sayı giriniz. Lütfen!'))

#sorgu = sayi >0 and sayi <100
#print(sorgu)

sorgu = ((sayi>0) and (sayi<100)) and (sayi%2 == 0)
email = 'turkalp'
passw = '12345'
emailch = input('email adresinizi giriniz')
passch = input('Şifrenizi giriniz')

sorgu = (email == emailch) and (passw == passch)


print(sorgu)

