# _*_ coding: utf8 _*_
#dört elemanlı bir liste oluşturuldu
liste = ["Bmw","Mercedes","Opel","Mazda"]
#listenin eleman sayısı yazdırıldı
result = len(liste)
#listenin ilk ve son elemanları yazdırıldı
result = liste[0] +" "+ liste[len(liste)-1]
#listenin indis numarasıyla elemanı değiştirrildi 
liste[-1] = "Toyota"
result = liste
# liste içinde elemanın olup olmadığını kontrol etme
result = "Mercedes" in liste
result = "Audi" in liste
#listenin başlangıçtan belli bir indis numarasına kadar yazdırmak için kullanılır
result = liste[0:3]
result = liste[:3]
#listenin son iki elemanını değiştirmek için kullanılabilir 
liste[-2:] = ["Toyota","Renault"]
result = liste
#burada liste üzerine görüntüde eleman eklemsi yapmak için kullanılır 
#burada yapılan ekleme listenin ilk halinde ki eleman sayısını değiştirmez 
result = liste + ["Audi", "Nissan"]
#sonuncu elemanı silmek yada eleman silmek için del komutu kullanılır
del liste[-1]
result = liste
# bir listeyi tersten yazdırmak için kullanılabilir
result = liste[::-1]

studentA = ["Yiğit","Bilgi",12,[12,45,78]]
studentB = ["Sena","Turan",45,[78,98,23]]
studentC = ["Mahmut", "Türkalp",24,[14,5,95]]
result = studentA[0] + str(studentB[2])
result = studentB[3][2]
result = "Öğrenci C'nin adı/ soyadı {0} {1}\n ve yaşı {2}".format(studentC[0],studentC[1],str(studentC[2]))
result = float(studentB[3][0] + studentB[3][1] +studentB[3][2])/3
print(result)
