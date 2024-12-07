from arquivo import *
from caixa import caixa

produtos = abrir_arquivo()
if produtos != []:
    caixa(produtos)
