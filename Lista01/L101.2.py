

class Circulo:
    def __init__(self, raio):
        self.raio = raio

    def area(self):
        return 3.14 * self.raio **2



raio = float(input("Digite o raio do círculo: "))
circulo = Circulo(raio)
print(f"A área do círculo é : {circulo.area():.2f}")

