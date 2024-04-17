# Arvores Binarias de procura

class No:
         # construtor
        def __init__(self, valor=None, esq=None, dir=None):
                self.valor = valor
                self.esq = esq
                self.dir = dir

def insOrd(raiz, val):
        if( raiz is None):
                return No(val)
        if(raiz.valor > val):
                raiz.esq = insOrd(raiz.esq, val)
        else:
                raiz.dir = insOrd(raiz.dir, val)
        return raiz

def find(raiz, val):
        if( raiz is None):
                return False
        if(raiz.valor == val):
                return True
        if(raiz.valor > val):
                return insOrd(raiz.esq, val)
        else:
                 return insOrd(raiz.dir, val)

def pre_ordem(raiz, exp):
        if( raiz is None):
                return exp
        esquerda = pre_ordem(raiz.esq, exp)
        direita  = pre_ordem(raiz.dir, exp)
        return exp + [raiz.valor] + esquerda + direita

def in_ordem(raiz, exp):
        if( raiz is None):
                return exp
        esquerda = in_ordem(raiz.esq, exp)
        direita  = in_ordem(raiz.dir, exp)
        return exp + esquerda + [raiz.valor] + direita

def pos_ordem(raiz, exp):
        if( raiz is None):
                return exp
        esquerda = in_ordem(raiz.esq, exp)
        direita  = in_ordem(raiz.dir, exp)
        return exp + esquerda + direita + [raiz.valor]

# imprime lista ligada
def printa(inicio):
    a = inicio
    while(a is not None):
        print(a.valor)
        a = a.prox

# main prog
raiz = None
raiz = insOrd(raiz, 5)
raiz = insOrd(raiz, 7)
raiz = insOrd(raiz, 3)
raiz = insOrd(raiz, 1)
raiz = insOrd(raiz, 2)
raiz = insOrd(raiz, 8)
lista = in_ordem(raiz,[])
print(lista)
lista = pre_ordem(raiz,[])
print(lista)
lista = pos_ordem(raiz,[])
print(lista)
