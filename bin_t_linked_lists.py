class No:
    #constructor
    def __init__(self, valor=None, esq=None, dir=None):
        self.valor = valor
        self.esq = esq
        self.dir = dir

def insOrd(raiz, val):
    if(raiz is None):
        return No(val)
    if(raiz.valor > val):
        raiz.esq = insOrd(raiz.esq, val)
    else:
        raiz.dir = insOrd(raiz.dir, val)
    return raiz

# imprime lista ligada
def printa(inicio):
    a = inicio
    while(a is not None):
        print(a.valor)
        a = a.esq

newList = insOrd(None, 5)
newList = insOrd(newList, 3)
newList = insOrd(newList, 2)
printa(newList)
