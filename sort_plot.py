import time
import random
import matplotlib.pyplot as plt
import numpy as np


def insertionSort (V):
    N = len(V)
    for j in range(1,N):
        key = V[j]
        i = j - 1
        while (i >= 0 and V[i] > key):
	        V[i+1] = V[i];
	        i -= 1
        V[i+1] = key;



def bubbleSort (V):
    j=0
    ok=False
    N = len(V)
    while (not ok):
        ok = True
        for i in range(N-1,j,-1):
            if (V[i-1] > V[i]):
                #swap
                V[i-1], V[i] = V[i], V[i-1] 
                ok = False
        j += 1

def bubbleSort2(V):
    N = len(V)
    for i in range(N-1,0,-1):
        for j in range(0,i):
            if (V[j] > V[j+1]):
	            #swap
                V[j], V[j+1] = V[j+1], V[j] 



def shellSort (V, gaps):
    N = len(V)
    for h in gaps:
        for i in range(h, N):
            key = V[i]
            j = i
            while( j >= h and V[j - h] > key ):
                V[j] = V[j - h]
                j -= h
            V[j] = key



def mergeSort(V, i, f):
    if(i < f):    
        m = i + (f - i) // 2
        mergeSort(V, i, m,)
        mergeSort(V, m+1, f)
        merge(V, i, m, f)

def merge(V, i, m, f):
    n1 = m - i + 1
    n2 = f - m

    #fazer auxs e copiar V[] para eles
    N = [0] * n1
    M = [0] * n2
    for j in range(0, n1):
        N[j] = V[i + j]
    for j in range(0, n2):
        M[j] = V[m + 1 + j]

    #fusao  (a->idx de N[], b-> idx de M[], k->idx de V[])
    a = 0
    b = 0
    k = i
    while(a < n1 and b < n2):
        if(N[a] < M[b]):
            V[k] = N[a]
            a += 1
        else:
            V[k] = M[b]
            b += 1 
        k += 1
     
    # copiar resto dos arrays para V[]
    while a < n1:
        V[k] = N[a]
        k += 1
        a += 1
    while b < n2:
        V[k] = M[b]
        k += 1
        b += 1

# assume que aux e inicalmente uma copia de V
def mergeSort2(V, aux, i, f):
    if(i < f):    
        m = i + (f - i) // 2
        mergeSort2(aux, V, i, m,)
        mergeSort2(aux, V, m+1, f)  # alterna nos papeis de aux[] e V[]
        merge2(V, aux, i, m, f)

def merge2(V, aux, i, m, f):

    #fusao
    a = i
    b = m + 1 
    for k in range(i,f+1): 
        if(a > m):
            aux[k] = V[b] 
            b += 1
        else:
            if(b > f):
                aux[k] = V[a] 
                a += 1
            else:
                if(V[b] < V[a]):
                    aux[k] = V[b]
                    b += 1
                else:
                    aux[k] = V[a]
                    a += 1
     


def quickSort (V, i, f):
    if(i < f):    
        pivot = partition(V,i,f)
        quickSort(V, i, pivot-1)
        quickSort(V, pivot+1, f)

# particao de Lomuto (mais simples)
def partition (V, i, f):
    # choose the rightmost element as pivot
    pivot = V[i]
 
    # pointer for greater element
    a = i
 
    # traverse through all elements
    # compare each element with pivot
    for b in range(i+1, f+1):
        if V[b] <= pivot:
 
            # If element smaller than pivot is found
            # swap it with the greater element pointed by i
            a = a + 1
 
            # Swapping element at a with element at b
            (V[a], V[b]) = (V[b], V[a])
 
    # Swap the pivot element with the greater element specified by a
    (V[a], V[i]) = (V[i], V[a])
 
    # Return the position from where partition is done
    return a 

def quickSort2(V, i, f):
    if(i < f):    
        pivot = partition2(V,i,f)
        quickSort2(V, i, pivot-1)
        quickSort2(V, pivot+1, f)

# original de Hoare. produz melhores particoes (mais estaveis).
# tipicamente faz 3 x menos swaps que Lomuto...
def partition2(V, i, f):
    p = V[i]  # pivot no leftmost
    a = i
    b = f + 1
    # atravessar array e comparar com pivot
    while(True):
        while(True):
            a += 1
            if(a > f or V[a] >= p): break   # until
        while(True):
            b -= 1
            if(b < i or V[b] <= p): break  # until

        if(a >= b): break    # until
        V[a], V[b] = V[b], V[a]

    V[b], V[i] = V[i], V[b]
    return b      # retorna pos do pivot


def quickSort3(A, i, f):
	if(i >= f):
		return
	k = random.randint(i, f) # escolhe pivot
	A[k], A[i] = A[i], A[k]
	me, ma = partition3(A, i, f)
	quickSort3(A, i, me - 1)
	quickSort3(A, ma + 1, f)


def partition3(A, i, f):       # particao ideal para listas com poucos duplicados
    menors = i       # menores que pivot
    x = i
    maiors = f       # maiores que pivot
    pivot = A[i]     # pivot ccomo o primeiro do array (random na funcao QS3)
    while (x <= maiors):      # a comecar no primeiro elemento
        if(A[x] < pivot):
            A[menors], A[x] = A[x], A[menors]
            menors += 1
            x += 1
        elif(A[x] > pivot):
            A[x], A[maiors] = A[maiors], A[x]
            maiors -= 1
        else:
            x += 1	
    return menors, maiors         # agora retorna dois indices!



def countingSort(A, N, k):   # assume-se que A[1..N]
    # faz array B[]
    B = [0]
    for i in range(1,N+1):
        B += [0]
    C = [0]
    for i in range(1,k+1):
        C += [0]

    for i in range(1,N+1):
        C[A[i]] += 1
    for i in range(1,k+1):  # acumulado!
        C[i] += C[i-1]
    for j in range(N,0,-1):
        B[C[A[j]]] = A[j]
        C[A[j]] -= 1

    return B



# programa principal
print()
print()


# gera lista
# Muito havera a fazer aqui... tipo de distribuicao, gama de valores, tamanho, ocorrencia de duplicados, etc...
# exemplo para fazer grafico de desempenho de 3 algoritmos
NTrails = 20
gaps = [701,301,132,57,23,10,4,1]
Gama = 1000

# lista tam=10
print("N=10")
V = []
for i in range(1,11):  #   lista de N elementos (a variar nas vossas experiencias)
    V += [random.randrange(1,Gama+1)]  # gama de valores 
# benchmark
XX = []
res = []
res2 = []
res3 = []
tot = 0.0
tot2 = 0.0
tot3 = 0.0

for i in range(1,NTrails+1):
    A = V.copy()
    st = time.process_time()
    insertionSort(A)
    en = time.process_time()
    tot += (en-st)
    A = V.copy()
    st = time.process_time()
    shellSort(A,gaps)
    en = time.process_time()
    tot2 += (en-st)
    A = V.copy()
    aux = V.copy()
    st = time.process_time()
    mergeSort2(A,aux,0,len(A)-1)
    en = time.process_time()
    tot3 += (en-st)
res +=[tot]
res2 +=[tot2]
res3 +=[tot3]
XX += [10]


# lista tam=100
print("N=100")
V = []
for i in range(1,101):  #   lista de N elementos (a variar nas vossas experiencias)
    V += [random.randrange(1,Gama+1)]  # gama de valores 
# benchmark
tot = 0.0
tot2 = 0.0
tot3 = 0.0
for i in range(1,NTrails+1):
    A = V.copy()
    st = time.process_time()
    insertionSort(A)
    en = time.process_time()
    tot += (en-st)
    A = V.copy()
    st = time.process_time()
    shellSort(A,gaps)
    en = time.process_time()
    tot2 += (en-st)
    A = V.copy()
    aux = V.copy()
    st = time.process_time()
    mergeSort2(A,aux,0,len(A)-1)
    en = time.process_time()
    tot3 += (en-st)
res +=[tot]
res2 +=[tot2]
res3 +=[tot3]
XX += [100]


print("Computacao demorada...")
# listas >= 1000
size = 1000
while(size < 20001):
    print("N="+str(size))
    V = []
    for i in range(1,size+1):  #   lista de N elementos (a variar nas vossas experiencias)
        V += [random.randrange(1,Gama+1)]  # gama de valores


    # benchmark
    tot = 0.0
    tot2 = 0.0
    tot3 = 0.0
    for i in range(1,NTrails+1):
        A = V.copy()
        st = time.process_time()
        insertionSort(A)
        en = time.process_time()
        tot += (en-st)
        A = V.copy()
        st = time.process_time()
        shellSort(A,gaps)
        en = time.process_time()
        tot2 += (en-st)
        A = V.copy()
        aux = V.copy()
        st = time.process_time()
        mergeSort2(A,aux,0,len(A)-1)
        en = time.process_time()
        tot3 += (en-st)
    res +=[tot]
    res2 +=[tot2]
    res3 +=[tot3]
    XX += [size]

    size *= 2  # dobrar tamanho o anterior...

# fazer plot
print(XX)
print(res)
print(res2)
print(res3)

fig, ax = plt.subplots()
plt.title('Comparing Algorithms', loc='left', fontsize=22)
plt.xlabel('Input (#N)')
plt.ylabel('Time (sec)')

ax.plot(XX, res, color='blue', linewidth=1.0, label='insertionSort')
ax.plot(XX, res2, color='green', linewidth=1.0, label='ShellSort')
ax.plot(XX, res3, color='red', linewidth=1.0, label='mergeSort2')

ax.set(xlim=(0, 10000), xticks=np.arange(1, 20000,2000),
       ylim=(0, 100), yticks=np.arange(1, 150,10))

ax.legend()
plt.show()
