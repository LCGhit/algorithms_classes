class Celula:
    # construtor
    def __init__(self, ant=None, val=None, prox=None):
        self.val = val
        self.ant = ant
        self.prox = prox


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
    return(connectedList)


def printa(connectedList):
    complete = 0
    if connectedList.prox != 0:
        complete = complete + connectedList.val + 10*(printa(connectedList.prox))
    else:
        complete = complete + connectedList.val
    return complete

linkedListValues = []
def invert_list(linkedList):
    if linkedList.prox != 0:
        linkedListValues.append(linkedList.val)
        invert_list(linkedList.prox)
        linkedList.val = linkedListValues[0]
        linkedListValues.pop(0)
    else:
        linkedListValues.append(linkedList.val)
        linkedList.val = linkedListValues[0]
        linkedListValues.pop(0)
    return linkedList


def sumLists(list1, list2, overflow):
    total = 0
    elementsSum = list1.val + list2.val + overflow
    if elementsSum >= 10:
        rest = elementsSum%10
        overflow = elementsSum//10
        try:
            total =+ rest
            total = total + 10*(sumLists(list1.prox, list2.prox, overflow))
        except:
            return elementsSum
    else:
        try:
            total =+ elementsSum
            total = total + 10*(sumLists(list1.prox, list2.prox, 0))
        except:
            return elementsSum
    return total

inicio = Celula(0,5,0)
inicio_2 = Celula(0,8,0)
inicio = insertBefore(inicio, 7)
inicio_2 = insertBefore(inicio_2, 9)
inicio = insertBefore(inicio, 3)
inicio_2 = insertBefore(inicio_2, 2)
inicio = insertBefore(inicio, 8)
inicio_2 = insertBefore(inicio_2, 1)

inverted_inicio = invert_list(inicio)
inverted_inicio_2 = invert_list(inicio_2)

firstList = printa(inverted_inicio)
secondList = printa(inverted_inicio_2)
print(firstList, "+", secondList)

newVar = sumLists(invert_list(inicio), invert_list(inicio_2), 0)
print(newVar)
