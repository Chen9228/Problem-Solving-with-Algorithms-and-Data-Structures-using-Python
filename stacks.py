class Stack:
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    def push(self,item):
        return self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[-1]
    def size(self):
        return len(self.items)




# 检查符号是否对称
def parChecker(symbolString):
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol in "{([":
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                top = s.pop()
                if not matches(top,symbol):
                    balanced = False
        index = index + 1
    if s.isEmpty() and balanced:
        return True
    else:
        return False
def matches(open,close):
    opens = "([{"
    closers = ")]}"
    return opens.index(open) == closers.index(close)


# 10进制转2进制
def divideBy2(number):
    remStack = Stack()
    while number > 0:
        rem = number % 2
        remStack.push(rem)
        number = number//2
    binaryString = ""
    while remStack.isEmpty() == False:
        binaryString = binaryString+str(remStack.pop())
    return binaryString

# 进制转换
def baseConverter(number,base):
    digits = "0123456789ABCDEF"
    remStack = Stack()
    while number > 0:
        rem = number % base
        remStack.push(rem)
        number = number//base
    newString = ""
    while remStack.isEmpty() == False:
        newString = newString+digits[remStack.pop()]
    return newString



# Infix-to-Postfix

def infixToPostfix(infixexpr):
    prec = {}
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    opStack = Stack()
    postfixList = []
    tokenList = infixexpr.split()
    for token in tokenList:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            postfixList.append(token)
        elif token == '(':
            opStack.push(token)
        elif token == ')':
            topToken = opStack.pop()
            while topToken != '(':
                postfixList.append(topToken)
                topToken = opStack.pop()
        else:
            while (not opStack.isEmpty()) and \
               (prec[opStack.peek()] >= prec[token]):
                  postfixList.append(opStack.pop())
            opStack.push(token)
    while not opStack.isEmpty():
        postfixList.append(opStack.pop())
    return " ".join(postfixList)

# Postfix Evaluation 

def postfixEval(postfixExpr):
    operandStack = Stack()
    tokenList = postfixExpr.split()

    for token in tokenList:
        if token in "0123456789":
            operandStack.push(int(token))
        else:
            operand2 = operandStack.pop()
            operand1 = operandStack.pop()
            result = doMath(token,operand1,operand2)
            operandStack.push(result)
    return operandStack.pop()

def doMath(op, op1, op2):
    if op == "*":
        return op1 * op2
    elif op == "/":
        return op1 / op2
    elif op == "+":
        return op1 + op2
    else:
        return op1 - op2


















if __name__ == "__main__":
    # s = Stack()
    # print(s.isEmpty())
    # s.push(4)
    # s.push('dog')
    # print(s.peek())
    # s.push(True)
    # print(s.size())
    # print(s.isEmpty())
    # s.push(8.4)
    # print(s.pop())
    # print(s.pop())
    # print(s.size())
    # print(parChecker('((()))'))
    # print(parChecker('(()'))
    # print(parChecker('{{([][])}()}'))
    # print(parChecker('[{()]'))
    # print(divideBy2(42))
    # print(divideBy2(233))
    # print(baseConverter(25,2))
    # print(baseConverter(256,16))
    # print(baseConverter(25,8))
    print(infixToPostfix("( A + B ) * C - ( D - E ) * ( F + G )"))