from arquivo import *
from caixa import caixa

produtos = abrir_arquivo()
if produtos != []:
    produtos = caixa(produtos)
gravar_arquivo(produtos)

# instalar python-tabulate para o programa funcionar: pip install tabulate