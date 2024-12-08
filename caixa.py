from tabulate import tabulate
from utils import *

def controle_caixa (produtos_disponiveis):
    produtos = produtos_disponiveis
    itens_cliente = []
    flag = msg_iniciar_atendimento()
    while flag:
        imprimir_produtos(produtos)
        id_produto = entrar_id(produtos)
        produtos, itens_cliente = adicionar_produto(produtos, id_produto, itens_cliente)
        flag = msg_finalizar_atendimento()
    imprimir_nota_cliente (itens_cliente)
    return itens_cliente

def adicionar_produto(produtos, id_produto, itens_cliente):
    for produto in produtos:
        if produto[0] == id_produto:
            print(f"{produto[1]} está sendo adicionado.")
            quantidade = entrar_quantidade(produto)
            produtos = remover_produto_estoque(produtos, id_produto, quantidade)
            # copia o produto e adiciona ao carrinho
            add_produto = produto[:]
            add_produto[2] = quantidade
            itens_cliente.append(add_produto)
            print(f"{produto[1]} foi adicionado.")
    return produtos, itens_cliente

def caixa(produtos):
    clientes = []
    while True:
        itens_cliente = controle_caixa(produtos)
        clientes.append(itens_cliente)
        if msg_fechar_caixa():
            break
    # mostrar_caixa(clientes)

def imprimir_nota_cliente(cliente):
    tabela = []
    total_cliente = 0
    for item in cliente:
        id_item, nome, quantidade, preco = item
        total = quantidade * preco
        tabela.append([id_item, nome, quantidade, preco, total])
        total_cliente += total

    print(tabulate(tabela, headers=["Item", "Produto", "Quant.", "Preço", "Total"], tablefmt="grid"))
    print(f"Itens: {len(cliente)}")
    print(f"Total: {total_cliente}")

    
    