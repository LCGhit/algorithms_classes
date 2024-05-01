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

def fixRight(A):
    B = A.dir
    if(B.bal == -1):
        A.bal = B.bal = 0
        A = RotateLeft(A)
    else:
        C = B.esq
        match C.bal:
            case 1:
                A.bal = 0
                B.bal = -1
            case -1:
                A.bal = 1
                B.bal = 0
            case 0:
                A.bal = B.bal = 0
        C.bal = 0
        A.dir = RotateRight(B)
        A = RotateLeft(A)
    return A
