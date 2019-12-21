def usalma(num):

    def inner(power):
        return num**power
    return inner
#ilk başta yapılan buy işlmele beraber usalma fonkuna değer verilir
#daha sonra inner ı yani içteki fonku çağırmak için ise print içindeki işlem gerçeklerştirilir
#buradaki temel amaç ilkinde ana fonku çağırmak ikincide ise içteki fonku çağırıp işlem döndürmektir
two = usalma(2)
print(two(3))


def yetki_sorgu(page):
    def inner(role):
        if role == "admin":
            return f"{role} rolünün {page} sayfasına ulaşabilir"
        else:
            return f"{role} istenilen sayfaya ulaşılamaz"
    return inner
damin = yetki_sorgu("Product")
print(damin("user"))

def islem (istek):
    def toplam(*args):
        toplam = 0
        for i in args:
            toplam += i
        return toplam
    def carpma(*args):
        carpim = 1
        for i in args:
            carpim *=i
        return carpim
    if istek == "toplam":
        return toplam
    else:
        return carpma

toplama = islem("toplam")
print(toplama(1,5,78,98))
