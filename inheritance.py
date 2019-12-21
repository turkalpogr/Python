#inheritance miras bırakma
"""
buradaki temel amaç her yerde aynı kodları tekrar tekrar yazmaktansa
tek seferde yazıp her yewrde kullanmak
"""
class Person():
    def __init__(self, fname,lname):
        self.fname = fname
        self.lname = lname
        print('Person Created {0} {1}'.format(fname,lname))
    def who_am(self):
        print("I'm a person")
"""
inheritance yaparken person classından özelliklerini miras alan 
Student class ı person ın içinde yer almayan diğer çzelliklerde eklenerek kullanılabilir
bunun yanında override yaparak personın içinden gelen bazı özellikleri ezerek başka biçim yada şekillerde kullanbiliriz
inheritance ın en büyük karı zamandır ve hafızadır
"""
class Student(Person):

    def __init__(self,fname,lname):
        Person.__init__(self,fname,lname)
        print("Student Created")
    #override
    def who_am(self):
        print("lalalalla")
    def sayHEllo(self):
        print("Hello")

p = Person('Deneme', 'lalalal')
s = Student('Mahmut', 'Türkalp')
s.who_am()
s.sayHEllo()

print(f"{s.fname} {s.lname}")

print("**************************************")
class Teacher(Person):
    def __init__(self,fname, lname,brans):
        super().__init__(fname, lname)
        self.brans = brans
    def who_am(self):
        print("teacher {}".format(self.brans))

t = Teacher('Mahmut', 'Türkalp','Bilişim')
t.who_am()