#class oluşturma
class Person:
    #attribute class ve  object olmak üzere ikiye ayrılır
    #constructer
    #java yada diğer dillerden farklı olarak this yapısını init içindeki girilmiş olan ilk parametre karşılıyor
    #illa ilk parametre self olmak zorunda değildir herhangi bir dildeki alışkın olunan yapılarda kullanılabilir
    #örneğin this gibi yapılar kullanılabilir
    #buradaki amaç dışardan gelecek olan değeri içeride
    #rahatça çalıştırabilmektir
    #bunun yanında init daima çalıştırılacak olan bir yapıdır
    #yani class için oluşturulmuş olan her instance için ayrı olarak çağırmaya gerek duymadan çalışır demektir

    def __init__(self, name, year):
        self.name = name
        self.year = year
        print(f"{year} ve {name}")
        print("init metodu çalıştı")
    def selam(self):
        return 'hello'
    #method
#object instance
p = Person('Mahmut',24)
print(f"{p.name}, {p.selam()}")
print(p.year)
