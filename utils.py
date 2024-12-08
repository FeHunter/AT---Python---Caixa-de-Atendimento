def msg_iniciar_atendimento ():
    while True:
        resposta = input("Iniciar atendimento? S|N : ")
        if (resposta.lower() == "s"):
            return True
        elif (resposta.lower() == "n"):
            return False
        else:
            print("Entrada inválida")

def msg_finalizar_atendimento ():
    while True:
        resposta = input("Finalizar atendimento? S|N : ")
        if (resposta.lower() == "s"):
            return False
        elif (resposta.lower() == "n"):
            return True
        else:
            print("Entrada inválida")

def entrar_quantidade (produto):
    while True:
        try:
            qtd = int(input("Digite a quantidade do produto: "))
            if (qtd > 0):
                if verificar_estoque(produto, qtd):
                    return qtd
                else:
                    print("Estoque insuficiente")
            else:
                print("A quantidade tem que ser maior que zero")
        except:
            print("Entrada inválida")

def entrar_id (produtos):
    try:
        while True:
            id = int(input("Digite o id do produto: "))
            if pesquisar_id(produtos, id):
                produto = produto_pelo_id(produtos, id)
                if produto[2] > 0:
                    return id
                else:
                    print("Produto sem estoque")
    except:
        print("Entrada inválida")
    
def pesquisar_id (produtos, id):
    '''
    faz a busca pelo id do produto dentro da lista de produtos, caso encontre retorna o id se não retorna -1
    '''
    for produto in produtos:
        if (produto[0] == id):
            return True
    print("ID não localizado")
    return False

def verificar_estoque(produto, quantidade):
    '''
    Recebe o produto e quantidade informada e verificar se o estoque e suficiente
    '''
    if int(produto[2]) >= int(quantidade):
        return True
    else:
        return False
            
def remover_produto_estoque (produtos, id, quantidade):
    for produto in produtos:
        if produto[0] == id:
            produto[2] -= quantidade
    return produtos

def produto_pelo_id (produtos, id):
    for produto in produtos:
        if produto[0] == id:
            return produto

def imprimir_produtos (produtos):
    for produto in produtos:
        print(f"{produto}")

