def greeting(name):
    print("hello", name)


print(greeting("ali"))
print(greeting)

def outer(num1):
    print("outer")
    def inner_inc(num1):
        print("inner")
        return num1+1
    num2 = inner_inc(num1)
    print(num2 , num1)
outer(11)

def fac(number):
    def inFac(number):
        if number <= 1:
            return 1
        return number*inFac(number-1)
    return inFac(number)

print(fac(5))