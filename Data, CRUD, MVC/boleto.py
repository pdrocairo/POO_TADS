from datetime import datetime
from enum import Enum

class Pagamento(Enum):
    EM_ABERTO = 1
    PAGO_PARCIAL = 2
    PAGO = 3

class Boleto():
    def __init__(self, codBarras, dataEmissao, dataVencimento, dataPayment, valorBoleto, valorPago):
        self.codBarras = codBarras
        self.dataEmissao = dataEmissao
        self.dataVencimento = dataVencimento
        self.dataPayment = dataPayment
        self.valorBoleto = valorBoleto
        self.valorPago = valorPago
        

    def pagar(self, valor):
        self.valorPago = valor
        self.dataPayment = datetime.now()


    def situacao(self):
        if self.valorPago <= 0:
            return Pagamento.EM_ABERTO.name
        elif self.valorPago < self.valorBoleto:
            return Pagamento.PAGO_PARCIAL.name
        else:
            return Pagamento.PAGO.name
    
    def __str__(self):
        return (
            f"Código de barras: {self.codBarras}\n"
            f"Data de emissão: {self.dataEmissao}\n"
            f"Data de vencimento: {self.dataVencimento}\n"
            f"Data de pagamento: {self.dataPayment}\n"
            f"Valor do boleto: {self.valorBoleto}\n"
            f"Valor pago: {self.valorPago}\n"
            f"Situação: {self.situacao()}"
        )
    


# 1. Boleto em aberto
b1 = Boleto(
    codBarras="1234567890",
    dataEmissao=datetime(2026, 4, 1),
    dataVencimento=datetime(2026, 4, 30),
    dataPayment=None,
    valorBoleto=100.0,
    valorPago=40.0,
)

print(b1)




