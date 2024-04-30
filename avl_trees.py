class NoAVL:
    def __init__(self, valor=None, bal=0, esq=None, dir=None):
        self.valor = valor
        self.esq = esq
        self.dir = dir
        self.bal = bal

def RotateRight(A):
    B = A.esq
    A.esq = B.dir
    B.dir = A
    return B

def RotateLeft(B):
    A = B.dir
    B.dir = A.esq
    A.esq = B
    return A
