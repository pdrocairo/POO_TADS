# CÍRCULO:
# A classe deve ter um atributo raio para armazenar a dimensão da figura e métodos para calcular sua área e sua
# circunferência.
# Escrever um programa para testar a classe.

class Circulo:
    def __init__(self, raio):
        self.raio = raio

    def area(self):
        return 3.14 * self.raio **2
    
    def circunferencia(self):
        return 2 * (3.14 * self.raio)



raio = float(input("Digite o raio do círculo: "))
circulo = Circulo(raio)
print(f"A área do círculo é: {circulo.area():.2f}")
print(f"A circunferencia é: {circulo.circunferencia():.2f}")
