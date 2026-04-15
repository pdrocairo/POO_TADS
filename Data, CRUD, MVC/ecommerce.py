
import os

class Cliente:
    def __init__(self, nome, telefone, email, ident):
        self.__nome = nome
        self.__telefone = telefone
        self.__email = email
        self.__ident = ident
        
    def set_ident(self, ident):
        self.__ident = ident

    def get_ident(self):
        return self.__ident


    def set_nome(self, nome):
        self.__nome = nome

    def get_nome(self):
        return self.__nome
    
    def set_telefone(self, telefone):
        self.__telefone = telefone

    def get_telefone(self):
        return self.__telefone

    def set_email(self, email):
        self.__email = email

    def get_email(self):
        return self.__email

class UI:
    def __init__(self):
        self.lista_clientes = []

    @staticmethod
    def menu():
        print("Escolha uma opçao: \n")
        print("1 - Criar Usuário")
        print("2 - Deletar Usuário")
        print("3 - Atualizar usuário")
        print("4 - Listar Usuários")
        print("5 - Sair")
        return input("Digite o número da opçao: ")
    
    @staticmethod
    def atualizar_menu():
        print("\n------------------------------------------")
        print("1 - Atualizar email")
        print("2 - Atualizar telefone")
        print("3 - Atualizar nome")
        print("4 - Sair")
        print("------------------------------------------\n")
        return input("Digite o número da opçao: ")
    
    @staticmethod 
    def checar_opcao_menu2(opcao):
        if opcao.isnumeric():
            if int(opcao) < 1 or int(opcao) > 4:
                return True
        elif opcao.isalpha():
            return True       
    @staticmethod 
    def checar_valor_menu2():
        opcao = UI.atualizar_menu()
        while UI.checar_opcao_menu2(opcao):
            print("Valor inválido")
            opcao = UI.atualizar_menu()
        return int(opcao)

    @staticmethod
    def clear():
        os.system('cls' if os.name == 'nt' else 'clear')
    
    @staticmethod
    def checar_opcao(opcao):
        if opcao.isnumeric():
            if int(opcao) < 1 or int(opcao) > 5:
                return True
        elif opcao.isalpha():
            return True
        
    @staticmethod    
    def checar_valor_menu():
        valor_menu = UI.menu()
        while UI.checar_opcao(valor_menu):
            print("Valor Inválido")
            valor_menu = UI.menu()
        return int(valor_menu)
        
    
    
    def criar_cliente(self):
        nome = input("\nDigite o nome do cliente: ")
        telefone = input("Digite o telefone do cliente: ")
        email = input("Digite o email do cliente: ")
        ident = input("Digite o id do cliente: ")
        return Cliente(nome, telefone, email, ident)
        

    def salvar_cliente(self, cliente):
        self.lista_clientes.append(cliente)

    def mostrar_clientes(self):
        if len(self.lista_clientes) > 0:
            for cliente in self.lista_clientes:
                print("\n--------------------------------------------------------------------------------")
                print(f"ID {cliente.get_ident()} - Nome: {cliente.get_nome()} -  Telefone: {cliente.get_telefone()} -  Email: {cliente.get_email()},")
                print("----------------------------------------------------------------------------------\n")
        else:
            print("\n----------------------------------------")
            print("\nNENHUM USUÁRIO CADASTRADO\n")
            print("----------------------------------------\n")


    def apagar_cliente(self):
        if len(self.lista_clientes) > 0:
            ident = input("Digite o ID do cliente a deletar: ")
            for cliente in self.lista_clientes:
                if ident == cliente.get_ident():
                    self.lista_clientes.remove(cliente)
        else:
            print("\n----------------------------------------")
            print("\nNENHUM USUÁRIO CADASTRADO\n")
            print("----------------------------------------\n")

    def atualizar_cliente(self):
        if len(self.lista_clientes) > 0:
            opcao = UI.checar_valor_menu2()

            if opcao == 4:
                print("\nSaindo da Atualizaçao...")
                return
            ident = input("Digite o ID do cliente a ser atualizado: ")
            cliente_encontrado = False
            for cliente in self.lista_clientes:
                if ident == cliente.get_ident():
                    cliente_encontrado = True
                    self.clear()
                    if opcao == 1:
                        novo_email = input("Digite o novo email: ")
                        cliente.set_email(novo_email)
                    if opcao == 2:
                        novo_telefone = input("Digite o novo numero de telefone: ")
                        cliente.set_telefone(novo_telefone)
                    if opcao == 3:
                        novo_nome = input("Digite o nome do cliente: ")
                        cliente.set_nome(novo_nome)

            if not cliente_encontrado:
                print("\n----------------------------------------")
                print("\nNENHUM USUÁRIO ENCONTRADO\n")
                print("----------------------------------------\n")
                    
        else:
            print("\n----------------------------------------")
            print("\nNENHUM USUÁRIO CADASTRADO\n")
            print("----------------------------------------\n")

    
    def ToString(self):
        return f"ID {self.get_ident()}, Nome: {self.get_nome()}, Telefone: {self.get_telefone()}, email = {self.get_email()},"


    def main(self):
        while True:
            valor = UI.checar_valor_menu()
            self.clear()
            if valor == 1:
                self.clear()
                cliente = self.criar_cliente()
                self.clear()
                self.salvar_cliente(cliente)
                self.clear()
            if valor == 2:
                self.clear()
                self.apagar_cliente()
                self.clear()
            if valor == 3:
                self.atualizar_cliente()
            if valor == 4:
                self.clear()
                self.mostrar_clientes()
            if valor == 5:
                break
    
            

interface = UI()
interface.main()       




