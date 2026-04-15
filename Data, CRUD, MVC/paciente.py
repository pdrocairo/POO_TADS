from datetime import datetime


class Paciente:
    def __init__(self, nome, cpf, nascimento, telefone):
        self.__nome = nome
        self.__cpf = cpf
        self.__nascimento = nascimento
        self.__telefone = telefone

    def set_nome(self, nome):
        self.__nome = nome
    
    def get_nome(self):
        return self.__nome
    
    def set_cpf(self, cpf):
        self.__cpf = cpf
    
    def get_cpf(self):
        return self.__cpf
    
    def set_nascimento(self, nascimento):
        self.__nascimento = nascimento
    
    def get_nascimento(self):
        return self.__nascimento
    
    def set_telefone(self, telefone):
        self.__telefone = telefone
    
    def get_telefone(self):
        return self.__nome
    
    def idade(self):
        data_atual = datetime.now()
        data_atual = data_atual.date()

        dia_nascimento, mes_nascimento, ano_nascimento = self.__nascimento.split("/")
        ano_nascimento = int(ano_nascimento)
        mes_nascimento = int(mes_nascimento)
        dia_nascimento = int(dia_nascimento)

        calc_ano = data_atual.year - ano_nascimento
        calc_mes = data_atual.month - mes_nascimento
        if calc_mes < 0:
            calc_ano -= 1
            calc_mes += 12
        return f"{self.__nome} tem {calc_ano} anos e {calc_mes} meses de idade"


    def __str__(self):
        return f"O paciente {self.__nome} do cpf {self.__cpf} nasceu {self.__nascimento} e tem esse número para contato : {self.__telefone}"




geuda = Paciente("Geuda", "187.131.223-04", "21/03/1962", "84987851136")
cairo = Paciente("Cairo", "688.280.553-91", "10/12/1972", "84988940434")
pedro_cairo = Paciente("Pedro Cairo", "074.166.983-83", "13/01/2000", "84986299476")

print(cairo.idade())