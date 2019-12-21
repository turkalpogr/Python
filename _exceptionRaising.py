"""x = 10
if x > 5:
    raise Exception("x 5 ten büyük değer alama")
    en basit şekliyle exception bu şekilde fırlatılabilir

"""

def chech(self):
    import re
    if len(self) < 8:
        raise Exception("parola en az 8 karakterden oluşmalı")
    elif not re.search("[a-z]", self):
        raise Exception("parola küçük harf içermeli")
    elif not re.search("[A-Z]", self):
        raise Exception("parola büyük harf içermeli")
    elif not re.search("[0-9]", self):
        raise Exception("parola rakam içermeli")
    elif not re.search("[_@$]", self):
        raise Exception("parola alpha numeric olmalıdır")
    elif  re.search("\s", self):
        raise Exception("parola boşluklardan oluşamaz")
    else:
        print("geçerli parola")

passs = input("Lütfen parola oluşturun:")
den = passs.strip()
try:
    chech(passs)
except Exception as e:
    print(e)
else:
    print("geçerli parola")
