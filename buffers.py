#Listas ligadas
# varias operacoes

class Celula:
    # construtor
    def __init__(self, valor=None, prox=None):
        self.valor = valor
        self.prox = prox

# inserir novo elemento no inicio
def inserir_ini(inicio, novo):
    novo.prox = inicio
    return(novo)

def inserir_fim(inicio,novo):
    if(inicio is None):
        return novo
    pt = inicio
    while(pt.prox is not None):
        pt = pt.prox
    pt.prox = novo
    novo.prox = None
    return inicio

# apagar um valor dado
def delete(inicio,val):
        if(inicio is None):
                return None
        # e o primeiro elemento?
        if(inicio.valor == val):
                temp = inicio.prox
                inicio.prox = None
                return temp
        pt = inicio
        ant = pt
        while(pt is not None and pt.valor != val):
                ant = pt
                pt = pt.prox
        if(pt is not None):
                ant.prox = pt.prox
                pt.prox = None
                return inicio

# insercao ordenada
def insOrd(inicio, val):
    novo = Celula(val)
    if(inicio is None):
        return novo
    pt = inicio
    ant = pt
    while(pt is not None and val > pt.valor):
        ant = pt
        pt = pt.prox

    if(pt == inicio):
        novo.prox = pt
        inicio = novo
    else:
        novo.prox = pt
        ant.prox = novo
    return inicio


# imprime lista ligada
def printa(inicio):
    a = inicio
    while(a is not None):
        print(a.valor)
        a = a.prox


# main prog
eu = Celula(1.0)
ou = Celula(3.2)
inicio = eu
inicio = inserir_ini(inicio, ou)


# imprime lista ligada
printa(inicio)

print()

# inseriro no fim
eu = Celula(7.0)
ou = Celula(8.2)
inicio = inserir_fim(inicio, eu)
inicio = inserir_fim(inicio, ou)
inicio = inserir_fim(inicio, Celula(9.5))

printa(inicio)
print()

inicio = delete(inicio, 7.0)
printa(inicio)

print()

inicio = None
inicio = inserir_fim(inicio, Celula(9))
inicio = insOrd(inicio, 5)
inicio = insOrd(inicio, 3)
inicio = insOrd(inicio, 1)
inicio = insOrd(inicio, 8)
inicio = insOrd(inicio, 2)
printa(inicio)
print()

def invert_list(linkedList):
    firstValue = linkedList.valor
    if linkedList.prox != None:
        thisValue = linkedList.valor
        nextValue = invert_list(linkedList.prox)
        if (linkedList.valor < nextValue):
            linkedList.valor = nextValue
        return thisValue
    else:
        thisValue = linkedList.valor
        linkedList.valor = 9
        return thisValue


invert_list(inicio)
print("stuff")
printa(inicio)
