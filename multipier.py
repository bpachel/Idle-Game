from decimal import getcontext, Decimal

class Multipier():
    def __init__(self, val=0, tier=1, div=10):
        self.val = Decimal(val)/Decimal(div)
        self.tier = tier

    def __mul__(self, other):
        if isinstance(other, Multipier):
            if other.tier == self.tier:
                return self.val+other.val-1
            else:
                return self.val*other.val
        else:
            raise TypeError





if __name__ == '__main__':
    mult1 = Multipier(11, 1)
    mult2 = Multipier(11, 1, 10)
    mult3 = Multipier(11, 2)


    print(mult1*mult2)
    print(mult1*mult3)