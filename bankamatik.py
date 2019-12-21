#obje yapısı
hesapA = {
    'ad': 'Mahmut Türkalp',
    'hesapNo': 123456469,
    'bakiye': 2000,
    'ekhesap':3000
}
hesapB = {
    'ad': 'Musa Türkalp',
    'hesapNo': 1237756469,
    'bakiye': 4000,
    'ekhesap':354
}

def paraCek(hesap, miktar):
    print(f"Merhaba {hesap['ad']}")
    if hesap['bakiye'] >= miktar:
        hesap['bakiye'] -= miktar
        print("istediğiniz miktarı alabilirisiniz")
    else:
        toplam = hesap['bakiye'] + hesap['ekhesap']
        if(toplam >= miktar):
            ekhesap = input("ek hesabı kullanmak ister misin (e/h)")
            if(ekhesap == 'e'):
                bakiye = miktar - hesap['bakiye']
                hesap['bakiye'] = 0
                hesap['ekhesap'] -= bakiye
                print("paranızı alabilirsiniz")
                print(hesap['ekhesap'])
            else:
                print(f"{hesap['hesapNo']} nolu hesabınızda {hesap['bakiye']}")
        else:print("üzgünüz paranız yetersiz")
paraCek(hesapA,2300)
paraCek(hesapA,800)
