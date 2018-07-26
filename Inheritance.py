#### 继承
# 逻辑电路
### Logic Gate 分为 Binary Gate/Unary Gate
### Binary Gate :AND/OR
### Unary Gate : NOT

class LogicGate:
    def __init__(self,n):
        self.label = n
        self.output = None
    def getLabel(self):
        return self.label
    def getOutput(self):
        self.output = self.performGateLogic()
        return self.output

class BinaryGate(LogicGate):
    def __init__(self,n): #从父类继承初始化步骤
        LogicGate.__init__(self, n)
        self.pinA = None
        self.pinB = None
    def getPinA(self):
        if self.pinA == None:
            return int(input("Enter PIN A INPUT FOR GATE "+ self.getLabel()+"-->"))
        else:
            return self.pinA.getFrom().getOutput()
    def getPinB(self):
        if self.pinB == None:
            return int(input("Enter PIN B INPUT FOR GATE "+ self.getLabel()+"-->"))
        else:
            return self.pinB.getFrom().getOutput()
    def setNextPin(self,source):
        if self.pinA == None:
            self.pinA = source
        else:
            if self.pinB == None:
                self.pinB = source
            else:
                print('Cannot connect:NO EMPTY PINS')

class UnaryGate(LogicGate):
    def __init__(self,n):
        LogicGate.__init__(self, n)
        self.pin = None
    def getPin(self):
        if self.pin == 
        return int(input("Enter PIN INPUT FOR GATE "+self.getLabel()+"-->"))

class AndGate(BinaryGate):
    def __init__(self,n): #继承
        BinaryGate.__init__(self, n)
    def performGateLogic(self): # 自带部分
        a = self.getPinA()
        b = self.getPinB()
        if a==1 and b==1:
            return 1
        else:
            return 0

class OrGate(BinaryGate):
    def __init__(self,n):
        BinaryGate.__init__(self, n)
    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()
        if a == 1 or b == 1:
            return 1
        else:
            return 0

class NotGate(UnaryGate):
    def __init__(self,n):
        UnaryGate.__init__(self, n)
    def performGateLogic(self):
        a = self.getPin()
        if a == 1:
            return 0
        else:
            return 1

class Connector:
    def __init__(self,from_gate,to_gate):
        self.fromgate = from_gate
        self.togate = to_gate
        to_gate.setNextPin(self)

    def getFrom(self):
        return self.fromgate
    def getTo(self):
        return self.togate
