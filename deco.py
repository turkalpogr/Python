def mydeco(func):
    def wrqpper():
        print("fonksiyondan önce işlemler")
        func()
        print("sonraki özellikler")
    return wrqpper
#decorator fonksiyonlardaki genel amaç genel olarak tanımlanmış bir fonksiyonun özelliklerini diğer fonklarda kullanmaktır
#@mydeco yazınca hello = mydeco(hello) yapmaya gerek kalmıyor mydeco kendi tanımlayıpp hello üzerinde kendi değişimlerini yapıyot

@mydeco
def hello():
    print("hello")

def greet():
    print("greeet")

hello()