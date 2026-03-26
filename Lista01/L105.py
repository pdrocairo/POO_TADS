# Sistema de Checkout de Supermercado
# O Desafio: Criar uma classe Produto para gerenciar preços e descontos por quantidade (venda no atacado).

# Atributos: Nome do produto, preço unitário e quantidade em estoque.

# Método calcular_total(quantidade_compra): * Se o cliente comprar 10 unidades ou mais, ele ganha 10% de desconto no valor total.

# O método deve verificar se há estoque suficiente. Se não houver, retorna 0.

# Se houver estoque, subtrai a quantidade do atributo da classe e retorna o valor final a pagar.

# Dica: Use o return para entregar o valor final e trate a mensagem de "Sem estoque" no programa principal.


class Produto:
    def __init__(self, nome_produto, preco_unitario, quantidade_estoque):
        self.nome_produto = nome_produto
        self.preco_unitario = preco_unitario
        self.quantidade_estoque = quantidade_estoque

    def calcular_total(self, quantidade_compra):
        #verifica quantidade do estoque para progredir
        if quantidade_compra > 0 and quantidade_compra <= self.quantidade_estoque:

            valor_final = self.preco_unitario * quantidade_compra

            if quantidade_compra >= 10:
                valor_final = valor_final * 0.9

            self.quantidade_estoque -= quantidade_compra

            return valor_final
        
        else:
            return 0

produto = str(input("digite o produto: "))
preco = int(input("digite o preco do produto: "))
estoque = int(input("digite quantos tem no estoque: "))
quantidade= int(input("digite quantos produtos voce quer: "))

compra = Produto(produto, preco, estoque)

total = compra.calcular_total(quantidade)

if total > 0:
    print(f"Compra de {quantidade} {compra.nome_produto}s realizada!")
    print(f"Total a pagar (com desconto se aplicado): R$ {total:.2f}")
    print(f"Estoque atualizado: {compra.quantidade_estoque} unidades")
else:
    print("Erro: Quantidade inválida ou estoque insuficiente.")

        

        


