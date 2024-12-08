import pathlib

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
                id = int(campos[0])
                nome = campos[1]
                quantidade_estoque = int(campos[2])
                preco = float(campos[3])
                produtos.append([id, nome, quantidade_estoque, preco])
    except:
        print("Erro ao abrir o arquivo")
        return []
    
    return produtos

def gravar_arquivo(produtos):
    '''
    Grava os dados dos produtos em um arquivo produtos.csv
    '''
    dir_current = pathlib.Path(__file__).parent.resolve()
    arq = str(dir_current) + "//produtos.csv"
    try:
        with open(arq, "w", encoding="UTF-8") as arquivo:
            for produto in produtos:
                linha = f"{produto[0]},{produto[1]},{produto[2]},{produto[3]}\n"
                arquivo.write(linha)
    except:
        print("Erro ao salvar arquivo.")

