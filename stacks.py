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
    print(baseConverter(25,2))
    print(baseConverter(256,16))
    print(baseConverter(25,8))