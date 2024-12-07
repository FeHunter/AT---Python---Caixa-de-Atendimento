from utils import *

def adicionar_produtos (produtos):
    '''
    Adiciona os produtos a lista do cliente, remover o produto adicionado ao cliente do estoque e 
    retorna a lista de produtos e a lista do cliente atualizadas
    '''
    # imprimir_produtos(produtos)
    cliente = []
    flag = msg_iniciar_atendimento()
    while flag:
        id_produto = entrar_id()
        produto_valido = pesquisar_id(produtos, id_produto)
        if produto_valido:
            if verificar_estoque(produtos, id_produto):
                quantidade = entrar_quantidade()
                produto = produtos[id_produto]
                cliente.append({"produto": produto, "quantidade": quantidade})
                produtos = remover_produto_estoque(produtos, id_produto, quantidade)
            else:
                print(f"Produto [{produtos[id_produto][1]}] sem estoque.")
        else:
            print("Produto não encontrado.")
        flag = msg_finalizar_atendimento()
    return produtos, cliente

def caixa (produtos):
    '''
    Controla o sistema do caixa
    '''
    clientes = []
    produtos, cliente = adicionar_produtos(produtos)
    print(cliente)
    # imprimir_produtos(produtos)
    
    