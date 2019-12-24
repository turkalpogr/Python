def toplama(a,b):
    return  a+b
def cik(a,b):
    return a-b
def carp (a,b):
    return a*b
def bol(a,b):
    return a/b

def islem(f,f1,f2,f3, islem):
    if islem == "toplama":
        print(f(2,3))
    elif islem == "cik":
        print(f1(2,3))
    elif islem == "bol":
        print(f2(2,3))
    elif islem == "carp":
        print(f3(2,3))
    else: print("geçersiz işlem")
islem(toplama, cik, bol, carp,"toplama")

