from datetime import datetime

noww = datetime.now() # now ile today aynıdır Mantık olarak benzerlik gösterirler
result = datetime.ctime(noww)
result = datetime.strftime(noww, "%Y")
print(result)
print(noww.month)

#burada dikkat edilmesi gerekn husus şöyleki eğer ay adları Türkçe yazılırsa şayet hata verecektir
#bundan dollayı string bir ifade olrak belirtilen gün ay yıl hatta zaman objeşerinin ingilizceye uygun şekilde
#yazılması olabilecek bütün hataları engeller en azından strptime metodu kullanıldığında

t = "14 May 1995"
"""gun , ay , yil = t.split()
print(gun, ay, yil)"""
#javadaki simpledateformat metodundan daha kolay bir kullanımı var
#bu kullanımla verilen string ifadeyi raha bir şekilde formatlamak mümkündür
#javadan sonra en büyük rahatlığı ve zorluğu python un çok esnek bir dil oluşudur
dt = datetime.strptime(t, "%d %B %Y")
dt = dt.year
print(dt)
birt = datetime(1995, 5,14)
rs = datetime.timestamp(birt)
rs = datetime.fromtimestamp(rs)
rs = datetime.now() - birt
rs = rs.days
print(rs)