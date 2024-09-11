class Produto:
    def __init__(self, codigo, descricao, preco):
        self.codigo = codigo
        self.descricao = descricao
        self.acrescimo = 0
        self.desconto = 0
        self.preco = preco

class CarrinhoCompras:
    def __init__(self):
        self.produtos = []

    def adicionar_produto(self, codigo, descricao, preco):
        produto = Produto(codigo, descricao, preco)
        self.produtos.append(produto)

    def aplicar_acrescimo_produto(self, codigo, valor_acrescimo):
        for produto in self.produtos:
            if produto.codigo == codigo:
                produto.acrescimo += valor_acrescimo
                produto.preco += valor_acrescimo
                break

    def aplicar_desconto_produto(self, codigo, valor_desconto):
        for produto in self.produtos:
            if produto.codigo == codigo:
                produto.desconto += valor_desconto
                produto.preco -= valor_desconto
                break

    def distribuir_acrescimo_total(self, valor_acrescimo_total):
        if len(self.produtos) == 0:
            return
        valor_acrescimo_por_produto = valor_acrescimo_total / len(self.produtos)
        for produto in self.produtos:
            produto.acrescimo += valor_acrescimo_por_produto
            produto.preco += valor_acrescimo_por_produto

    def distribuir_desconto_total(self, valor_desconto_total):
        if len(self.produtos) == 0:
            return
        valor_desconto_por_produto = valor_desconto_total / len(self.produtos)
        for produto in self.produtos:
            produto.desconto += valor_desconto_por_produto
            produto.preco -= valor_desconto_por_produto

    def exibir_resumo_venda(self):
        total_desconto = sum(produto.desconto for produto in self.produtos)
        total_acrescimo = sum(produto.acrescimo for produto in self.produtos)
        valor_total_venda = sum(produto.preco for produto in self.produtos)
        print("\nCarrinho de Compras:")
        for produto in self.produtos:
            print(f"Código: {produto.codigo}, Descrição: {produto.descricao}, Preço: {produto.preco:.2f}, Acréscimo: {produto.acrescimo:.2f}, Desconto: {produto.desconto:.2f}")
        print(f"Desconto total: {total_desconto:.2f}")
        print(f"Acréscimo total: {total_acrescimo:.2f}")
        print(f"Valor total da venda: {valor_total_venda:.2f}")

def menu_principal():
    carrinho = CarrinhoCompras()

    while True:
        print("\nMenu Principal:")
        print("1 - Adicionar produto ao carrinho")
        print("2 - Aplicar acréscimo a produto")
        print("3 - Aplicar desconto a produto")
        print("4 - Distribuir acréscimo entre todos os produtos")
        print("5 - Distribuir desconto entre todos os produtos")
        print("6 - Finalizar compra e exibir resumo")
        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
            codigo = input("Digite o código do produto: ")
            descricao = input("Digite a descrição do produto: ")
            preco = float(input("Digite o valor do produto: "))
            carrinho.adicionar_produto(codigo, descricao, preco)

        elif opcao == 2:
            codigo = input("Digite o código do produto para aplicar acréscimo: ")
            valor_acrescimo = float(input("Digite o valor do acréscimo: "))
            carrinho.aplicar_acrescimo_produto(codigo, valor_acrescimo)

        elif opcao == 3:
            codigo = input("Digite o código do produto para aplicar desconto: ")
            valor_desconto = float(input("Digite o valor do desconto: "))
            carrinho.aplicar_desconto_produto(codigo, valor_desconto)

        elif opcao == 4:
            valor_acrescimo_total = float(input("Digite o valor total do acréscimo: "))
            carrinho.distribuir_acrescimo_total(valor_acrescimo_total)

        elif opcao == 5:
            valor_desconto_total = float(input("Digite o valor total do desconto: "))
            carrinho.distribuir_desconto_total(valor_desconto_total)

        elif opcao == 6:
            carrinho.exibir_resumo_venda()
            break

        else:
            print("Opção inválida. Tente novamente.")

menu_principal()
