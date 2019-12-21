def usalma(num):

    def inner(power):
        return num**power
    return inner
two = usalma(2)
print(two(3))
