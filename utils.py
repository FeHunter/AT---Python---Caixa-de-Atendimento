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

def entrar_quantidade ():
    while True:
        try:
            qtd = int(input("Digite a quantidade do produto: "))
            if (qtd > 0):
                return qtd
            else:
                print("A quantidade tem que ser maior que zero")
        except:
            print("Entrada inválida")

def entrar_id ():
    return int(input("Digite o id do produto: "))
    
def pesquisar_id (produtos, id):
    '''
    faz a busca pelo id do produto dentro da lista de produtos, caso encontre retorna o id se não retorna -1
    '''
    imprimir_produtos(produtos)
    for produto in produtos:
        if (produto[0] == id):
            return id
    print("ID não localizado")
    return -1

def verificar_estoque(produtos, id):
    for produto in produtos:
        if (produto[0] == id and produto[2] > 0):
            return True
        else:
            return False
            
def remover_produto_estoque (produtos, id, quantidade):
    for produto in produtos:
        produto[2] -= quantidade
    return produtos
    
    
    
# remover depois
def imprimir_produtos (produtos):
    for produto in produtos:
        print(f"[ produto ]")