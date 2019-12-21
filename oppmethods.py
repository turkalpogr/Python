class Circle:
    pi = 3.14

    def __init__(self, yaricap = 1):
        self.yaricap = yaricap

    def cevre(self):
        return 2*self.pi*self.yaricap
    def alan(self):
        return self.pi*(self.yaricap**2)

c = Circle()
c2 = Circle(5)

print(f"alanı: {c2.alan()} ve çevre: {c2.cevre()} ")
