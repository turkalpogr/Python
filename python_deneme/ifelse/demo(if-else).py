name = input('Kullanıcı adınızı giriniz')
age = int(input('yaşınızı giriniz'))
edu = input('Eğitim bilgilerinizi giriniz')

if age >18 :
    if (edu.lower() == 'üniversite') or (edu.lower() == 'lise'):
        print("Ehliyet almak için bir sakıncanız bulunmamaktadır")
    else:
        print("Eğitim düzeyiniz ehliyet almak için yeterli değildir")
else:
    print("Ehliyet almak için yaşınız tutmamaktadır")
