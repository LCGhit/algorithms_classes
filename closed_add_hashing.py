#Closed Addressing hashing: implementação e avaliação
#Implementar Hashing usando closed addressing para tratar colisões.
#Implementar as operações de inserção, consulta, remoção e rehashing quando o fator de carga é ultrapassado.
#Apresentar complexidade amortizada.
#Testar com vários conjuntos de dados com diferentes distribuições e número de colisões.
#Implementar uma versão para números inteiros com dois exemplos de funções de hash.
#A implementação tem necessariamente de usar listas duplamente ligadas.

class Celula:
    # construtor
    def __init__(self, key=None, val=None, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

def printa(connectedList):
    if (connectedList.val == None and connectedList.next == None):
        return " "
    elif connectedList.val == None:
        complete = printa(connectedList.next)
    elif connectedList.next == None:
        complete = "Key: " + connectedList.key + " Value: "  + connectedList.val
    else:
        complete = "Key: " + connectedList.key + " Value: "  + connectedList.val + "\n " + (printa(connectedList.next))
    return complete

def hashFun_1(input):
    if not isinstance(input, int):
        num = 0
        for l in input:
            num = num + ord(l) - 96
        return num//3
    else:
        return input//3

def solveCollision(list, item):
    if list.next == None:
        list.next = item
        item.prev = list
    elif list.val == None:
        oldNext = list.next
        oldPrev = list.prev
        list = item
        list.next = oldNext
        list.prev = oldPrev
    else:
        solveCollision(list.next, item)
    return list

def addItem(array, key, value):
    address = hashFun_1(key)
    if array[address] == None:
        array[address] = Celula(key, value, 0, None)
    else:
        array[address] = solveCollision(array[address], Celula(key, value, 0, None))

def printTable(array):
    count = 0
    for i in array:
        if i != None:
            print("Index:", count, "\n", printa(array[count]))
        count += 1

def searchCollision(list, key):
    if list.key == key:
        return list
    else:
        return searchCollision(list.next, key)

def search(array, key):
    address = hashFun_1(key)
    if array[address] == None:
        return None
    elif array[address].key != key:
        return searchCollision(array[address].next, key)
    else:
        return array[address]

def delete(array, key):
    index = search(array, key)
    index.val = None
    index.key = None
    print(index)

closedAddr = [None] *30
addItem(closedAddr, "abc", "First")
addItem(closedAddr, "cba", "Second")
addItem(closedAddr, "bca", "Third")
addItem(closedAddr, "aaa", "Fourth")
addItem(closedAddr, "ccb", "Fifth")
addItem(closedAddr, "arst", "Sixth")
printTable(closedAddr)

delete(closedAddr, "bca")
printTable(closedAddr)
addItem(closedAddr, "bca", "newone")
printTable(closedAddr)
