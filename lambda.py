def square(a):
    return a * a


numbers = [1, 2, 3, 4, 5, 6]

result = list(map(square, numbers))

print(result)
# bu yöntemdeki mantık for vs kullanmadan daha kısa biçimde dizi elemanlarını bir fonksiyona atamaya ve değer döndürmeye yarar

for x in map(square, numbers):
    print(x)

# bu da python daki lambda yapıları
#aynı zamanda lambda yapıları bir değişkene atama yapıp sanki bir fonksiyon yazılmış gibide kullanılabilir
# java yada diğer dillere göre çok daha esnek bir yapıya sahip

result = list(map(lambda x: x * x, numbers))

print(result)
def check_even(num):
    return num %2 ==0
result = list(filter(check_even, numbers))

print(result)
re = list(filter(lambda x : x%2==0 , numbers))
print(re)