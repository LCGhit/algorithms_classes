class No:
    def __init__(self, valor=None, esq=None, dir=None):
        self.valor = valor
        self.esq = esq
        self.dir = dir

def insOrd(raiz, val):
    if raiz == None:
        return No(val)
    if val > raiz.valor:
        raiz.dir = insOrd(raiz.dir, val)
    else:
        raiz.esq = insOrd(raiz.esq, val)
    return raiz

def printAll(list, drawing):
    print(list.valor)
    if list.dir != None:
        drawing = drawing + "  "
        printAll(list.dir, drawing)
    if list.esq != None:
        drawing = drawing + "  "
        printAll(list.esq, drawing)

newList = No(35)
for i in [20,21,22,23,10,9,8,7,19,18,17,16,15,40,41,39]:
    insOrd(newList, i)

def treeHeight(root):
    count = 0
    if root == None:
        return 0
    countRight = 1+treeHeight(root.dir)
    countLeft = 1+treeHeight(root.esq)
    if countRight > countLeft:
        count = countRight
    else:
        count = countLeft
    return count
# print(treeHeight(newList))

def countNodes(root, node):
    count = ""
    if root == None:
        return ""
    if node > 1:
        count = str(countNodes(root.esq, node-1)) + " "*5
        count = count + str(countNodes(root.dir, node-1))
    else:
        return root.valor
    return count

def printTree(tree):
    count = 20
    for i in range(1, treeHeight(tree)+1):
        print(" "*count, countNodes(tree, i))
        count = count - 4

print("THE TREE\n")
printTree(newList)
lvl = input("What level would you like to see?\n=> ")
print("\nLVL " + lvl + " NODES:")
print(countNodes(newList, int(lvl)))
print("\nTREE HEIGHT:")
print(treeHeight(newList))
