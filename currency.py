from decimal import Decimal

class Currency():
    '''
    Klasa definiująca typ walut gry, takich jak złoto i punkty doświadczenia

    atrybuty:
    val - wartość typu Decimal
    type - string z typem waluty

    to do:
    ustalić jakie waluty wystąpią w finalnym produkcie i dodać sprawdzanie poprawności typu do konstruktora
    '''
    def __init__(self, val=0, type='gold'):
        self.val = Decimal(val)
        self.type = type

    def __mul__(self, other):
        if isinstance(other, Currency):
            if other.type == self.type:
                return self.val*other.val
            else:
                raise TypeError
        elif isinstance(other, Decimal) or isinstance(other, int):
            return self.val*other
        else:
            raise TypeError

    def __add__(self, other):
        if isinstance(other, Currency):
            if other.type == self.type:
                return self.val+other.val
            else:
                raise TypeError
        elif isinstance(other, Decimal) or isinstance(other, int):
            return self.val+other
        else:
            raise TypeError

    def __sub__(self, other):
        if isinstance(other, Currency):
            if other.type == self.type:
                return self.val-other.val
            else:
                raise TypeError
        elif isinstance(other, Decimal) or isinstance(other, int):
            return self.val-other
        else:
            raise TypeError

    def __rsub__(self, other):
        if isinstance(other, Currency):
            if other.type == self.type:
                return other.val - self.val
            else:
                raise TypeError
        elif isinstance(other, Decimal) or isinstance(other, int):
            return other - self.val
        else:
            raise TypeError

    def __truediv__(self, other):
        if isinstance(other, Currency):
            if other.type == self.type:
                return self.val/other.val
            else:
                raise TypeError
        elif isinstance(other, Decimal) or isinstance(other, int):
            return self.val/other
        else:
            raise TypeError

    def __rtruediv__(self, other):
        if isinstance(other, Currency):
            if other.type == self.type:
                return other.val/self.val
            else:
                raise TypeError
        elif isinstance(other, Decimal) or isinstance(other, int):
            return other/self.val
        else:
            raise TypeError

    def __lt__(self, other):
        if isinstance(other, Currency):
            if other.type == self.type:
                return self.val < other.val
            else:
                raise TypeError
        elif isinstance(other, Decimal) or isinstance(other, int):
            return self.val < other
        else:
            raise TypeError

    def __le__(self, other):
        if isinstance(other, Currency):
            if other.type == self.type:
                return self.val <= other.val
            else:
                raise TypeError
        elif isinstance(other, Decimal) or isinstance(other, int):
            return self.val <= other
        else:
            raise TypeError

    def __eq__(self, other):
        if isinstance(other, Currency):
            if other.type == self.type:
                return self.val == other.val
            else:
                raise TypeError
        elif isinstance(other, Decimal) or isinstance(other, int):
            return self.val == other
        else:
            raise TypeError

    def __ne__(self, other):
        if isinstance(other, Currency):
            if other.type == self.type:
                return self.val != other.val
            else:
                raise TypeError
        elif isinstance(other, Decimal) or isinstance(other, int):
            return self.val != other
        else:
            raise TypeError

    def __gt__(self, other):
        if isinstance(other, Currency):
            if other.type == self.type:
                return self.val > other.val
            else:
                raise TypeError
        elif isinstance(other, Decimal) or isinstance(other, int):
            return self.val > other
        else:
            raise TypeError

    def __ge__(self, other):
        if isinstance(other, Currency):
            if other.type == self.type:
                return self.val >= other.val
            else:
                raise TypeError
        elif isinstance(other, Decimal) or isinstance(other, int):
            return self.val >= other
        else:
            raise TypeError

    __rmul__ = __mul__
    __radd__ = __add__


if __name__ == '__main__':
    gold1 = Currency(100)
    gold2 = Currency(2)

    print('test mnożenia')
    print(gold1*3)
    print(3*gold1)
    print(gold2*gold1)

    print('\ntest dodawania')
    print(gold1 + 3)
    print(3 + gold1)
    print(gold2 + gold1)

    print('\ntest odejmowania')
    print(gold1 - 3)
    print(300 - gold1)
    print(gold1 - gold2)

    print('\ntest dzielenia')
    print(gold1/3)
    print(300/gold1)
    print(gold1/gold2)

    print('\ntest >')
    print(gold1 > 3)
    print(300 > gold1)
    print(gold1 > gold2)

    print('\ntest >=')
    print(gold1 >= 3)
    print(300 >= gold1)
    print(gold1 >= gold2)

    print('\ntest <=')
    print(gold1 < 3)
    print(300 < gold1)
    print(gold1 < gold2)

    print('\ntest <=')
    print(gold1 <= 3)
    print(300 <= gold1)
    print(gold1 <= gold2)

    print('\ntest ==')
    print(gold1 == 3)
    print(300 == gold1)
    print(gold1 == gold2)


