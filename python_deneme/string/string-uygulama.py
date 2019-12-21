#_*_ coding: utf8 _*_

website = "http://www.sadikturan.com"
course = "Ptyhon Kursu: Baştan Sona Python Programlama Rehberiniz (40 Saat)"
#cevap 1****************************************************************************
deneme = ' Hello world '
print(deneme)
deneme = deneme.strip()
print(deneme)
deneme = deneme.lstrip()
print(deneme)
deneme = deneme.rstrip()
print(deneme)
#cevap 2 ***************************************************************************
#strip yapısı aynı zamanda regex e de duyarlı çalışıyor yani parantez içine yazılan 
# değişken yada ifadelere göre silmede yapıyor
deneme = website.strip('htp:/')
print(deneme)
#cevap 3 ***************************************************************************
# count fonk ile saydırma yapabiliriz
# bu saydırmanın yanında aralık vererekte aralık içinden saydırma yapabiliriz
#deneme = website.count('w',2,15) örnek olarak verilebilir

deneme = website.count('w')
print(deneme)
deneme = course.find('Python')
print(deneme)
#nesenenin sayısal olup olmadığını sorgular
deneme = course.isdigit()
print(deneme)
#nesnenin sayısal olup olmadığını sorgular
deneme = 'Mahmut'.isalpha()
print(deneme)
#bu bölümde sağdan veya soldan veya ortadan yazıyı hizalama için kullanılır
#center ortalar
#ljust sola yaslar
#rjust sağa yaslayarak yazıyı yazar 
#ikinci parametre ise oluşruluşmuş olan boşluklara ne geleceğini belirler
deneme = 'Mahmut'.center(50,'*')
print(deneme)
deneme = 'mahmut'.ljust(50,'*')
print(deneme)
deneme = 'Mahmut'.rjust(50,'*')
print(deneme)
#üçüncü parametre ile kaç tane değişim yapılacağı belirlenir eğer bir sayı girilmezse tamamını değiştirir
deneme = course.replace(' ','*',5)
print(deneme)
deneme = 'Hello World'.replace('World','There')
print(deneme)
deneme = course.split(' ')
print(deneme)




