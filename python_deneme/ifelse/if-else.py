username = 'mahmut'
passw = '1324'

uCheck = input('Kullanıcı adını giriniz')
passwCheck = input('Şifrenizi giriniz')



isLoggedin = (username == uCheck)

if isLoggedin:
    if  (passw == passwCheck):
     print('hoş geldin')
    else :
        print('şifreniz yanlış')
else :
    print('Kullanıcı adınız hatalı')
