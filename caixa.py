from tabulate import tabulate
from utils import *

def controle_caixa (produtos):
    itens_cliente = []
    flag = msg_iniciar_atendimento()
    while flag:
        imprimir_produtos(produtos)
        id_produto = entrar_id(produtos)
        produtos, itens_cliente = adicionar_produto(produtos, id_produto, itens_cliente)
        flag = msg_finalizar_atendimento()
    return produtos, itens_cliente

def adicionar_produto(produtos, id_produto, itens_cliente):
    for produto in produtos:
        if produto[0] == id_produto:
            print(f"{produto[1]} está sendo adicionado.")
            quantidade = entrar_quantidade(produto)
            produtos = remover_produto_estoque(produtos, id_produto, quantidade)
            itens_cliente.append(produto)
            print(f"{produto[1]} foi adicionado.")
    return produtos, itens_cliente

def caixa(produtos):
    clientes = []
    while True:
        produtos, itens_cliente = controle_caixa(produtos)
        clientes.append(itens_cliente)
        if msg_fechar_caixa():
            break

    ctd_cliente = 1
    for cliente in clientes:
        tabela = []
        for item in cliente:
            id_item, nome, quantidade, preco = item
            total = quantidade * preco
            tabela.append([id_item, nome, quantidade, preco, total])

        msg_informacoes_cliente(ctd_cliente)
        print(tabulate(tabela, headers=["Item", "Produto", "Quant.", "Preço", "Total"], tablefmt="grid"))
        ctd_cliente += 1

    
    