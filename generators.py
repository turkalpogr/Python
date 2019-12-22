def cube():
    result = []
    for i in range(5):
        result.append(i**3)
    return result
print(cube())

def cube2():
    for i in range(50):
        yield i**3

for i in cube2():
    print(i)
#iterable objelerde ayrıyetten iter kullanmaya gerek yoktur direkt olarak next ile beraber liste elemanları yazılabilir

"""
kup = cube2()
iterator = iter(kup)

print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
"""