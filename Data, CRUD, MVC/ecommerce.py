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
        return input("Digite o número da opçao: ")
    
    @staticmethod
    def checar_opcao(opcao):
        if opcao.isnumeric():
            if int(opcao) < 1 or int(opcao) > 4:
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
        nome = input("Digite o nome do cliente: ")
        telefone = input("Digite o telefone do cliente: ")
        email = input("Digite o email do cliente: ")
        ident = input("Digite o id do cliente: ")
        return Cliente(nome, telefone, email, ident)
        

    def salvar_cliente(self, cliente):
        self.lista_clientes.append(cliente)

    def mostrar_clientes(self):
        if len(self.lista_clientes) > 0:
            for cliente in self.lista_clientes:
                print(f"ID {cliente.get_ident()}, Nome: {cliente.get_nome()}, Telefone: {cliente.get_telefone()}, email = {cliente.get_email},")
        else:
            print("\nNENHUM USUÁRIO CADASTRADO\n")


    def apagar_cliente(self):
        if len(self.lista_clientes) > 0:
            ident = input("Digite o ID do cliente a deletar: ")
            for cliente in self.lista_clientes:
                if ident == cliente.get_ident():
                    self.lista_clientes.remove(cliente)
        else:
            print("Nenhum usuário cadastrado")
    
    def main(self):
        while True:
            valor = UI.checar_valor_menu()
            if valor == 1:
                cliente = self.criar_cliente()
                self.salvar_cliente(cliente)
            if valor == 2:
                self.apagar_cliente()
            if valor == 4:
                self.mostrar_clientes()
            
            

interface = UI()
interface.main()       




