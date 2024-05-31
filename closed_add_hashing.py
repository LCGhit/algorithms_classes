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
        complete = "Key: " + str(connectedList.key) + " Value: "  + str(connectedList.val)
    else:
        complete = "Key: " + str(connectedList.key) + " Value: "  + str(connectedList.val) + "\n " + (printa(connectedList.next))
    return complete

def loadFactor(connectedList):
    if (connectedList.val == None and connectedList.next == None):
        return 0
    elif connectedList.val == None:
        load = loadFactor(connectedList.next)
    elif connectedList.next == None:
        load = 1
    else:
        load = 1 + loadFactor(connectedList.next)
    return load

def hashFun_1(input):
    if not isinstance(input, int):
        num = 0
        for l in input:
            num = num + ord(l) - 96
        return num//3
    else:
        return input//3

def hashFun_2(input):
    if not isinstance(input, int):
        num = 0
        for l in input:
            num = num + ord(l) - 96
        return num%3
    else:
        return input%3

def solveCollision(list, item):
    if list.next == None:
        list.next = item
        item.prev = list
    elif list.val == None:
        list.key = item.key
        list.val = item.val
    else:
        solveCollision(list.next, item)
    return list

def addItem(array, key, value, hashFunction):
    address = hashFunction(key)
    if array[address] == None:
        array[address] = Celula(key, value, 0, None)
    else:
        array[address] = solveCollision(array[address], Celula(key, value, 0, None))

def printTable(array):
    count = 0
    for i in array:
        if i != None:
            print("\nIndex:", count, "\n", printa(array[count]))
        count += 1

def getLoadFactor(array):
    add = 0
    count = 0
    for i in array:
        if i != None:
            add = add+loadFactor(array[count])
        count += 1
    print(add/len(array))
    return add/len(array)

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

def listDifference():
    print("\nFIRST DICT")
    closedAddr_1 = [None] *30
    addItem(closedAddr_1, "abc", "First", hashFun_1)
    addItem(closedAddr_1, "cba", "Second", hashFun_1)
    addItem(closedAddr_1, "bca", "Third", hashFun_1)
    addItem(closedAddr_1, "aaa", "Fourth", hashFun_1)
    addItem(closedAddr_1, "ccb", "Fifth", hashFun_1)
    addItem(closedAddr_1, "arst", "Sixth", hashFun_1)
    addItem(closedAddr_1, "tst", "Seventh", hashFun_1)
    addItem(closedAddr_1, "oie", "Eighth", hashFun_1)
    addItem(closedAddr_1, "ennn", "Ninth", hashFun_1)
    addItem(closedAddr_1, "ontl", "Tenth", hashFun_1)
    printTable(closedAddr_1)

    print("\nSECOND DICT")
    closedAddr_2 = [None] *30
    addItem(closedAddr_2, "Ana", "First", hashFun_1)
    addItem(closedAddr_2, "Maria", "Second", hashFun_1)
    addItem(closedAddr_2, "Antonio", "Third", hashFun_1)
    addItem(closedAddr_2, "Jose", "Fourth", hashFun_1)
    addItem(closedAddr_2, "Joao", "Fifth", hashFun_1)
    addItem(closedAddr_2, "Pedro", "Sixth", hashFun_1)
    addItem(closedAddr_2, "Pedro", "Seventh", hashFun_1)
    addItem(closedAddr_2, "Joana", "Eighth", hashFun_1)
    addItem(closedAddr_2, "Ines", "Ninth", hashFun_1)
    addItem(closedAddr_2, "Beatriz", "Tenth", hashFun_1)
    printTable(closedAddr_2)

def addDelete():
    closedAddr_1 = [None] *30
    addItem(closedAddr_1, "abc", "First", hashFun_1)
    addItem(closedAddr_1, "cba", "Second", hashFun_1)
    addItem(closedAddr_1, "bca", "Third", hashFun_1)
    addItem(closedAddr_1, "aaa", "Fourth", hashFun_1)
    addItem(closedAddr_1, "ccb", "Fifth", hashFun_1)
    addItem(closedAddr_1, "arst", "Sixth", hashFun_1)
    addItem(closedAddr_1, "tst", "Seventh", hashFun_1)
    addItem(closedAddr_1, "oie", "Eighth", hashFun_1)
    addItem(closedAddr_1, "ennn", "Ninth", hashFun_1)
    addItem(closedAddr_1, "ontl", "Tenth", hashFun_1)
    printTable(closedAddr_1)
    delete(closedAddr_1, "bca")
    printTable(closedAddr_1)
    addItem(closedAddr_1, "bca", "NEWONE", hashFun_1)
    printTable(closedAddr_1)

numArr = [3,55,2,98,2,4,61,44,53,22,34,70,1,86]

def hashDifference(array, hash1, hash2):
    arr1 = [None]*50
    arr2 = [None]*50
    for i in array:
        addItem(arr1, i, i, hash1)
        addItem(arr2, i, i, hash2)
    print("\n##########HASH 1##########")
    printTable(arr1)
    print("\n##########HASH 2##########")
    printTable(arr2)

def rehash(array):
    newArr = [None]*(len(array)+50)
    if getLoadFactor(array) > 0.4:
        count = 0
        for i in array:
            newArr[count] = i
            count += 1
    return newArr

a = [None]*25
addItem(a, "abc", "First", hashFun_1)
addItem(a, "cba", "Second", hashFun_1)
addItem(a, "cc", "Second", hashFun_1)
addItem(a, 5, "Second", hashFun_1)
addItem(a, "bca", "Third", hashFun_1)
addItem(a, "aaa", "Fourth", hashFun_1)
addItem(a, "ccb", "Fifth", hashFun_1)
addItem(a, "arst", "Sixth", hashFun_1)
addItem(a, "tst", "Seventh", hashFun_1)
addItem(a, "oie", "Eighth", hashFun_1)
addItem(a, "ennn", "Ninth", hashFun_1)
addItem(a, "ontl", "Tenth", hashFun_1)

#listDifference()
#addDelete()
#hashDifference(numArr, hashFun_1, hashFun_2)
#search(a, "ccb")
#getLoadFactor(a)
#a = rehash(a)
#getLoadFactor(a)
