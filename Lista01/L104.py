#  Segunda, terça e quinta, o valor base do ingresso é R$ 16,00.
#  Nas quartas todos pagam meia-entrada no valor de R$ 8,00, em qualquer horário.
#  Sexta, sábado e domingo, o valor base do ingresso é R$ 20,00.
#  Das 17h à meia-noite, há acréscimo de 50% no valor base do ingresso.

class EntradaCinema:
    def __init__(self, dia, horario):
        self.dia = dia
        self.horario = horario

    def inteira(self):
        if self.dia == "quarta":
            valorbase = 16
        elif self.dia in ["segunda", "terça", "quinta"]:
            return 16
        elif self.dia in ["sexta", "sabado", "domingo"]:
            valorbase = 20
        else:
            return 0
        
        if self.horario >= 17:
            valorbase *= 1.5

        return valorbase
    
    def meia(self):
        if self.dia == "quarta":
            return 8
        
        return self.inteira() / 2
    
dia_sessao = str(input("Digite o dia da semana: "))
hora_sessao = int(input("Digite o horario da sessao: "))

sessao = EntradaCinema(dia_sessao, hora_sessao)

precointeira = sessao.inteira()
precomeia = sessao.meia()

if precointeira == 0:
    print("Erro: Dia da semana inválido. Verifique a ortografia.")
else:
    print(f"\nSessão de {dia_sessao} às {hora_sessao}h:")
    print(f"Valor Inteira: R$ {precointeira:.2f}")
    print(f"Valor Meia-Entrada: R$ {precomeia:.2f}")