import pathlib

def produtos_mock ():
    produtos = [
        [1,"Produto 1", 1,10],
        [2,"Produto 2", 2,20],
        [3,"Produto 3", 3,30],
        [4,"Produto 4", 4,40],
        [5,"Produto 5", 5,50]
    ]
    return produtos

def abrir_arquivo ():
    '''
    Abrir o arquivo produtos.csv e retorna os produtos dentro de uma lista
    '''
    dir_current = pathlib.Path(__file__).parent.resolve()
    arq = str(dir_current) + "//produtos.csv"
    produtos = []
    try:
        with (open(arq, "r", encoding="UTF-8") as arquivo):
            while linha := arquivo.readline():
                campos = linha.strip("\n").split(",")
                id, nome, quantidade_estoque, preco = int(campos[0]), campos[1], int(campos[2]), float(campos[3])
                produtos.append(id, nome, quantidade_estoque, preco)
    except:
        print("Erro ao abrir o arquivo")
    
    return produtos

