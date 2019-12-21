import mod

result = mod.number
print(result)
result = mod.numbers
print(result)
result = mod.person["name"]
print(result)
result = mod.person["age"]
print(result)
p = mod.Person()
p.speak()

"""try:
    x = int(input())
    y= int(input())
    print(x/y)
except (ZeroDivisionError, ValueError) as e:
    print("ikinci sayı için 0 girilemz")
    print(e)"""
"""try:
    x = int(input())
    y= int(input())
    print(x/y)
except :
    print("hatalı")"""
while True:
    try:
        x = int(input())
        y= int(input())
        print(x/y)
    except Exception as e:
        print("Hata var")
        print(e)
    else:
        break
    finally:
        print("try ex bloğu sonlandı ")