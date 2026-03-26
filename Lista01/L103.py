# CONTA BANCARIA:
# A classe deve ter atributos para armazenar o nome do titular da conta, o número da conta e seu saldo e métodos
# para realizar as operações de depósito e saque.
# Escrever um programa para testar a classe.

class ContaBancaria:
    def __init__(self, nome, conta, saldo):
        self.nome = nome
        self.conta = conta
        self.saldo = saldo

    def deposito(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"O valor de {valor:.2f} foi adicionado ao seu saldo")
        else:
            print("O valor do depósito tem que ser de pelo menos R$0,01")

    def saque(self, valor):
        if saldo > 0:
            self.saldo -= valor
            print(f"Seu saque de {valor:.2f} foi efetuado com sucesso.")
        else:
            print("Voce precisa ter fundos positivos para efetuar um saque")






nome = str(input("Digite o nome do titular: "))
conta = int(input("Digite o numero da conta: "))
saldo = float(input("Digite seu saldo atual em conta: "))




valor_saque = float(input("Digite o Valor do Saque: "))
valor_deposito = float(input("Digite o Valor do Deposito: "))

conta_bancaria = ContaBancaria(nome, conta, saldo)
conta_bancaria.saque(valor_saque)
conta_bancaria.deposito(valor_deposito)