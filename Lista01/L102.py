# VIAGEM:
# A classe deve ter atributos para armazenar a distância em km e o tempo gasto em horas e minutos da viagem
# realizada. A classe deve possuir método para calcular a velocidade média atingida na viagem em km/h de acordo
# com a distância e o tempo gasto.
# Escrever um programa para testar a classe.

class Viagem:
    def __init__(self, distancia, horas, minutos):
        self.distancia = distancia
        self.horas = horas
        self.minutos = minutos

    def velocidade_media(self):
        tempo_total_horas = ((self.horas * 60) + self.minutos) / 60
        return self.distancia / tempo_total_horas
    
distancia = float(input("Digite a distância da viagem em km: "))
horas = int(input("Digite o tempo gasto em horas: "))
minutos = int(input("Digite o tempo gasto em minutos: "))

viagem = Viagem(distancia, horas, minutos)
print(f"Velocidade média da viagem: {viagem.velocidade_media():.2f} km/h")