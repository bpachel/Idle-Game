from decimal import getcontext, Decimal

getcontext().prec = 32

class Multipier():
    def __init__(self,val=Decimal(0), tier=1):
        self.val = Decimal(val)
        self.tier = tier

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
