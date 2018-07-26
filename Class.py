# Fraction Class
class Fraction(object):
    """docstring for Fraction"""
    def __init__(self, top,bottom): #初始化
        self.den = bottom
        self.num = top
    def show(self): #展示函数
        print(self.num,'/',self.den)
    # 重新定义__str__方法，后续可以使用print()
    def __str__(self):
        return str(self.num)+'/'+str(self.den)
    # arithmetic
    def __add__(self,fraction):
        newnum = self.num*fraction.den+self.den*fraction.num
        newden = self.den*fraction.den
        common = gcd(newnum, newden)
        return Fraction(newnum//common, newden//common)

    def __mul__(self,fraction):
        newnum = self.num*fraction.num
        newden = self.den*fraction.den
        common = gcd(newnum, newden)
        return Fraction(newnum//common, newden//common)

    def __sub__(self,fraction):
        newnum = self.num*fraction.den-self.den*fraction.num
        newden = self.den*fraction.den
        common = gcd(newnum, newden)
        return Fraction(newnum//common, newden//common)

    def __truediv__(self,fraction):
        newnum = self.num*fraction.den
        newden = self.den*fraction.num
        common = gcd(newnum, newden)
        return Fraction(newnum//common, newden//common)

    def __eq__(self,fraction):
        return self.num*fraction.den == self.den*fraction.num

    def __lt__(self,fraction):
        return self.num*fraction.den < self.den*fraction.num

    def __gt__(self,fraction):
        return self.num*fraction.den > self.den*fraction.num



# GCD -- Euclid Algoritm,求最大公约数
def gcd(m,n):
    while m%n != 0: #终止条件：余数为0
        d = m%n #取余数
        m = n # 互换
        n = d
    return n


# test part
if __name__ == "__main__":
    myf = Fraction(3,5)
    myf.show()
    print(myf)
    f1 = Fraction(1, 2)
    f2 = Fraction(1, 4)
    print(f1*f2)
    print(f1>f2)