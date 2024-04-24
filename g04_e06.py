class No:
    def __init__(self, valor=None, esq=None, dir=None):
        self.valor = valor
        self.esq = esq
        self.dir = dir

newList = No(35)

def insOrd(raiz, val):
    if raiz == None:
        return No(val)
    if val > raiz.valor:
        raiz.dir = insOrd(raiz.dir, val)
    else:
        raiz.esq = insOrd(raiz.esq, val)
    return raiz

insOrd(newList, 20)
insOrd(newList, 19)
insOrd(newList, 21)
insOrd(newList, 22)
insOrd(newList, 23)

def printa(list):
    print(list.valor)
    if list.dir != None:
        printa(list.dir)
    if list.esq != None:
        printa(list.esq)
# printa(newList)

def height(raiz, val):
    count = 0
    if raiz == None:
        return 0
    if val > raiz.valor:
        count = 1+height(raiz.dir, val)
    else:
        count = 1+height(raiz.esq, val)
    return count
print(height(newList, 4))
