class Stack:  # stack de inteiros usando um array

    # construtor
    def __init__(self, size=1):
        self.stack = []
        self.size = size
        for i in range(1,size):
            self.stack += [0]
        self.idx = 0

    def empty(self):
        return self.idx == 0

    def pop(self):
        if( not self.empty()):
            self.idx -= 1
            tmp = self.stack[self.idx]
            return tmp
        else:
            return None

    def push(self, x):
        if(self.idx < self.size):
            self.stack[self.idx] = x
            self.idx += 1

    def peek(self):
        if(not self.empty()):
            return self.stack[self.idx-1]


# main
s = Stack(10)
s.push(1)
s.push(2)
print(s.peek())
s.push(3)
print(s.peek())
s.pop()
print(s.peek())
print(s.empty())
s.pop()
print(s.peek())
s.push(3)
s.push('+')
s.push(5)
s.push(2)
s.push('/')
print()
print()
# while(not s.empty()):
#         print(s.pop())

def stackFun(element):
    print(element)
    s = Stack(10)
    for i in element:
        try:
            s.push(int(i))
        except:
            operand_1 = s.peek()
            s.pop()
            operand_2 = s.peek()
            s.pop()
            match i:
                case "+":
                    operation = operand_2 + operand_1
                    print(operand_2, "+", operand_1, "=", operation)
                    s.push(operation)
                case "-":
                    operation = operand_2 - operand_1
                    print(operand_2, "-", operand_1, "=", operation)
                    s.push(operation)
                case "/":
                    operation = operand_2 / operand_1
                    print(operand_2, "/", operand_1, "=", operation)
                    s.push(operation)
                case "*":
                    operation = operand_2 * operand_1
                    print(operand_2, "*", operand_1, "=", operation)
                    s.push(operation)
                case _:
                    return

    print(s.peek())

print("Result:")
stackFun(input())
