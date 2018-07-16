# Define Class

class Fraction(object):
    """abstract data type"""
    def __init__(self,top,bottom):
        self.num = top
        self.den = bottom
    def show(self):
        print(self.num,"/",self.den)
        
    












# test part
if __name__ == "__main__":
    my_fraction = Fraction(3,5)
    my_fraction.show()
    print(my_fraction)