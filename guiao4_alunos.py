class NoAVL:
	 # construtor
	def __init__(self, valor=None, bal = 0, esq=None, dir=None):
		self.valor = valor
		self.esq = esq
		self.dir = dir
		self.bal = bal # deve ser 1, 0, ou -1 para balanceado!

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
    if(B.bal == -1):   # RIGHT
        A.bal = B.bal = 0 # BAL
        A = RotateLeft(A)
    else:
        C = B.esq
        match C.bal:
            case  1:
                A.bal = 0
                B.bal = -1 #RIGHT
            case -1: 
                A.bal = 1  #LEFT
                B.bal = 0
            case  0: 
                A.bal = B.bal = 0
        C.bal = 0
        A.dir = RotateRight(B)
        A = RotateLeft(A)
    return A

def fixLeft(A):
    B = A.esq
    if(B.bal == 1):   # LEFT
        A.bal = B.bal = 0 # BAL
        A = RotateRight(A)
    else:
        C = B.dir
        match C.bal:
            case  1:
                A.bal = -1 #RIGHT
                B.bal = 0
            case -1: 
                A.bal = 0  
                B.bal = 1 #LEFT
            case  0: 
                A.bal = B.bal = 0
        C.bal = 0
        A.esq = RotateLeft(B)
        A = RotateRight(A)
    return A


def insAVL(raiz, vals, g):
    if(raiz is None):
        return 1, NoAVL(vals,0)
    else:
        if(raiz.valor > vals):
            g, raiz.esq = insAVL(raiz.esq, vals, g)
            if(g == 1):
                match raiz.bal: 
                    case 1: #LEFT 
                        raiz = fixLeft(raiz)
                        g = 0
                    case 0: 
                        raiz.bal = 1 # LEFT
                    case -1: #RIGHT 
                        raiz.bal = 0 # BAL
                        g = 0
        else:
            g, raiz.dir = insAVL(raiz.dir, vals, g)
            if(g == 1):
                match raiz.bal: 
                    case -1: #RIGHT 
                        raiz = fixRight(raiz)
                        g = 0
                    case 0: 
                        raiz.bal = -1 # RIGHT
                    case 1: #LEFT
                        raiz.bal = 0  # BAL
                        g = 0
    return g, raiz

# versao standard de BST
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





# exe 5
def find_menor(raiz):
    inicio = raiz
    temp = raiz.dir    # procura menor no lado dir (o seguinte ao que esta em raiz)
    while(temp is not None and temp.esq is not None):
        inicio = temp
        temp = temp.esq
    if(inicio != raiz):  # tem mais do que um filho?
        inicio.esq = temp.dir
    else:
        inicio.dir = temp.dir
    return temp.valor

def del_BT(raiz, x):
    if(raiz is None):
        return raiz
    if(raiz.valor == x):
        # caso raiz ser folha
        if(raiz.esq is None and raiz.dir is None):
            return None
        # caso lado dir ser vazio 
        if(raiz.esq is not None and raiz.dir is None):
            return raiz.esq
        # caso lado esq ser vazio 
        if(raiz.esq is None and raiz.dir is not None):
            return raiz.dir
        # caso raiz ter duas subarvores
        if(raiz.esq is not None and raiz.dir is not None):
            novo = find_menor(raiz)
            raiz.valor = novo
            return raiz
    else:
        if(raiz.valor < x):
            raiz.dir = del_BT(raiz.dir,x)
        if(raiz.valor > x):
            raiz.esq = del_BT(raiz.esq,x)
        return raiz

# exe 6
def deep(raiz):
    if(raiz is None):
        return 0
    else:
        t1 = 1 + deep(raiz.esq)
        t2 = 1 + deep(raiz.dir)
        return t1 if t1 > t2 else t2

def nivel(raiz, n):
    if(raiz is None):
        return []
    if( n == 1):
        return [raiz.valor]
    n -= 1
    L1 = nivel(raiz.esq, n)
    L2 = nivel(raiz.dir, n)
    return L1 + L2

# exe 7
def pr_tree(Raiz):
    n= deep(Raiz)
    for i in range(1,n+1):
        print(nivel(Raiz,i))



# exe 9

def bubble_up2(V, i):
	p = int((i - 1) / 2)   # antecessor de i
	while(i > 0 and V[i] > V[p]):
		V[i], V[p] = V[p], V[i]   # swap
		i = p
		p = int((i - 1) / 2)  # antecessor de i

def bubble_down2(V, N, i):
	f = 2*i + 1   # sucessor de i
	flag = False
	while(f < N and not flag):
		 # descendente da direita e menor?
		if(f+1 < N and V[f+1] > V[f]):
			f = f + 1
		if(V[f] < V[i]): 
			flag = True
		else:
			V[i], V[f] = V[f], V[i]  # swap
			i = f
			f = 2*i + 1   # sucessor de i

def heapify(V,N):
    for i in range(1,N):
        bubble_up2(V,i)

def heapSort(V):
    N = len(V)
    heapify(V,N)
    for i in range(N-1,-1,-1):
        V[0], V[i] = V[i], V[0]
        bubble_down2(V,i,0)



# exe 10
def verify_mheap(A):
    N = len(A)
    for x in range(0,N):
        i1 = 2*x + 1
        i2 = 2*x + 2
        if(i1 < N and A[x] > A[i1]):
                return False
        if(i2 < N and A[x] > A[i2]):
                return False

    return True



# main
b, raiz = insAVL(None,5,0)
b, raiz = insAVL(raiz,1,b)
b, raiz = insAVL(raiz,6,b)
b, raiz = insAVL(raiz,7,b)
b, raiz = insAVL(raiz,10,b)
b, raiz = insAVL(raiz,8,b)
b, raiz = insAVL(raiz,12,b)
b, raiz = insAVL(raiz,14,b)
b, raiz = insAVL(raiz,15,b)
b, raiz = insAVL(raiz,16,b)
b, raiz = insAVL(raiz,17,b)
b, raiz = insAVL(raiz,2,b)
print("AVL")
pr_tree(raiz)

print()

raiz = insOrd(None,5)
raiz = insOrd(raiz,1)
raiz = insOrd(raiz,6)
raiz = insOrd(raiz,7)
raiz = insOrd(raiz,10)
raiz = insOrd(raiz,8)
raiz = insOrd(raiz,12)
raiz = insOrd(raiz,14)
raiz = insOrd(raiz,15)
raiz = insOrd(raiz,16)
raiz = insOrd(raiz,17)
raiz = insOrd(raiz,2)
print("Standard")
pr_tree(raiz)

# testar delete em BT
raiz = del_BT(raiz,17)
print("apos delete  17")
pr_tree(raiz)
raiz = del_BT(raiz,5)
print("2 delete   5")
pr_tree(raiz)
raiz = del_BT(raiz,7)
print("3 delete   7")
pr_tree(raiz)

# teste verify_mheap()
A = [10,15,11,16,22,35,20,21,23,34,37,80,43,22,25,24,28]
print(A)
print(verify_mheap(A))
A = [10,15,11,16,22,35,20,21,23,34,37,80,43,22,25,24,28,12]
print(A)
print(verify_mheap(A))
# exe 12
print()
A = [3,5,1,2]
conta_BT(A)

# print de arvores ao longo de sequencia de insercoes
print()
b, raiz = insAVL(None,3,0)
b, raiz = insAVL(raiz,8,b)
pr_tree(raiz)
print()
b, raiz = insAVL(raiz,2,b)
pr_tree(raiz)
print()
b, raiz = insAVL(raiz,9,b)
pr_tree(raiz)
print()
b, raiz = insAVL(raiz,10,b)
pr_tree(raiz)
print()
b, raiz = insAVL(raiz,12,b)
pr_tree(raiz)
print()

#verifica se heapsort em ascendente
print()
A = [15,11,16,35,20,21,23,34,37,80,43,22,25,24,28,12,10]
heapSort(A)
print(A)
