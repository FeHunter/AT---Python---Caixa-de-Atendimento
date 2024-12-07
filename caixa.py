from utils import *

def adicionar_produtos (produtos):
    '''
    Adiciona os produtos a lista do cliente, depois volta lista do cliente com os produtos
    Remover o produto adicionado ao cliente do estoque
    Retorna a lista de produtos e a lista do cliente atualizadas
    '''
    # imprimir_produtos(produtos)
    cliente = []
    flag = msg_iniciar_atendimento()
    while flag == True:
        id_produto = entrar_id()
        if (pesquisar_id(produtos, id_produto) != -1):
            if (verificar_estoque(produtos, id_produto)):
                quantidade = entrar_quantidade()
                cliente.append([produtos[id_produto], quantidade])
                produtos = remover_produto_estoque(produtos, id_produto, quantidade)
            else:
                print("Produto sem estoque")
        flag = msg_finalizar_atendimento()
    return produtos, cliente

def caixa (produtos):
    '''
    Controla o sistema do caixa
    '''
    clientes = []
    produtos, cliente = adicionar_produtos(produtos)
    print(cliente)
    
    