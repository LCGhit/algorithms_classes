class Celula:
    # construtor
    def __init__(self, ant=None, val=None, prox=None):
        self.val = val
        self.ant = ant
        self.prox = prox

inicio = Celula(0,5,0)

def insertAfter(connectedList, element):
    element = Celula(0,element,0)
    connectedList.prox = element
    element.ant = connectedList
    return(element)

def insertBefore(connectedList, element):
    first = connectedList
    new = Celula(0,element,0)
    connectedList = new
    connectedList.prox = first
    return(new)

insertBefore(inicio, 7)

def printa(connectedList):
    if connectedList.prox != 0:
        print(connectedList.val)
        printa(connectedList.prox)
    else:
        print(connectedList.val)
printa(inicio)
