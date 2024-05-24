def is_min_heap(V):
    N = len(V)
    for i in range(0,N):
        if(2*i+1 < N and V[i] > V[2*i+1]):
            return False
        if(2*i+2 < N and V[i] > V[2*i+2]):
            print("no")
            return False
    print("yes")
    return True

A = [2,5,7,10,11,20,22]

is_min_heap(A)
