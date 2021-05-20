from hero import Hero, Item
from data_types import Currency
from decimal import Decimal
import random


class CurrencyContainer:
    def __init__(self, dif_level, forclass):
        # todo generowanie treasures - balans
        temp = ['might_exp', 'cunning_exp', 'psyche_exp', 'lore_exp']

        if forclass == 'Challenge':
            self.exp = [Currency(Decimal(random.randrange(100, 300, 1) / 100) * dif_level[i], i) for i in range(4)]
            self.riches = Currency(Decimal(random.randrange(200, 500, 1) / 100) * sum(dif_level), 'gold')
            self.treasures = Currency(0, 'treasure')

        # nagrody 3-5 razy wieksze niz w challenge
        if forclass == 'Adventure':
            self.exp = [Currency(Decimal(random.randrange(300, 1500, 1) / 100) * dif_level[i], i) for i in range(4)]
            self.riches = Currency(Decimal(random.randrange(600, 2500, 1) / 100) * sum(dif_level), 'gold')
            self.treasures = Currency(0, 'treasure')

        # interfejs wypisuje tylko niezerowe nagrody
        self.print_list = [i for i in self.exp if i.val > Decimal(0)]
        if self.riches.val > Decimal(0):
            self.print_list.append(self.riches)
        if self.treasures.val > Decimal(0):
            self.print_list.append(self.treasures)


itemNames = ['Weapon1', 'Weapon2']
itemTypes = ['Weapon', 'Helmet', 'Armor', 'Ring']

class ItemContainer:
    #lista przedmiotow za ukonczenie przygody. Dla challenge lista bedzie pusta
    def __init__(self, dif_level, challenges_count):
        self.items = []
        amount = random.randint(8, 12) * challenges_count // 50 # 1 item na 4-6 wyzwan
        for i in range(amount):
            #losowanie nazwy przedmiotu
            name = random.choice(itemNames)
            #losowanie typu przedmiotu
            type = random.choice(itemTypes)

            #todo balans ???????????
            #todo atrybuty aktywne wymagane do zalozenia

            #todo bonusy zalozonego itemu - 4 atrybuty aktywne w kolejnosci w liscie dif_level
            self.items.append(Item(name, type, minimum=[0, 0, 0, 0], m=0, c=0, p=0, l=0))


class Reward:
    # generowanie i przechowywanie nagrody za adventure/challenge
    def __init__(self, diff_level, type, challengesCount=0):
        self.waluta = CurrencyContainer(diff_level, type)
        self.items = ItemContainer(diff_level, challengesCount)

    def getItems(self):
        return self.items.items


# todo ustawienie parametrów losowania oraz
# aktualizacja wraz z postepem gry (coraz wyzsze przedzialy losowania)
# i generowanie coraz lepszych przedmiotow - tutaj czy w klasie Item????? - Lukasz wie

challenge_names = ["Wyzwanie1", "Walka z niedzwiedziem", "Przeplyniecie rzeki"]
adventure_names = ["Przygoda1", "Wyprawa w gory"]


class CampException(Exception):
    pass


class Challenge:  # wyzwanie
    def __init__(self, dif_level):
        self.name = random.choice(challenge_names)
        self.difficulty = [Decimal(random.randrange(50, 150, 1) / 100) * dif_level[i] for i in range(4)]
        self.reward = Reward(self.difficulty, 'Challenge')
        # self.type = type            #[False,False,False,False]
        #testowane 4 atrybuty aktywne
        self.cost = [Decimal(random.randrange(50, 100, 1) / 500) * self.difficulty[i] for i in range(4)]
        #piaty atrybut nieodpowiadajacy testowanym atrybutom todo balans
        self.cost.append(Decimal(random.randrange(50, 100, 1) / 1800 * sum(dif_level)))

    '''return true if completed challenge, false if not'''
    def onClock(self, bohater):
        temp_list = [bohater.passive[i].val - self.cost[i] for i in range(5)]
        for i in temp_list:
            if i < 0:
                raise CampException
        for i in range(5):
            bohater.passive[i].val -= self.cost[i]
        for i in bohater.passive:
            if i.val == 0:
                raise CampException
        for i in range(4):
            if self.difficulty[i] - bohater.active[i].val > 0:
                self.difficulty[i] -= bohater.active[i].val
            else:
                self.difficulty[i] = 0
        return self.difficulty == [0, 0, 0, 0]


class Adventure:  # przygoda
    def __init__(self, diff_level):
        self.name = random.choice(adventure_names)
        self.amount = random.randint(4, 20)
        self.challenges = [Challenge(diff_level) for i in range(self.amount)]
        self.challenge_index = 0
        self.in_action = False
        self.reward = Reward(diff_level, 'Adventure', self.amount)
        # todo pasek postepu przygody - gdzie?
        # todo pasek postepu danego wyzwania - gdzie?

    def start(self):
        self.in_action = True

    def stop(self):
        self.in_action = False

    '''Zwraca bool czy przygoda zostala ukonczona. 
    rzuca blad CampException jezeli trzeba zastopowac wszystkie przygody, bo wyczerpaly sie atrybuty pasywne.'''
    #todo Wtedy trzeba w nadrzednej metodzie wywolac metode stop dla wszystkich przygod gracza.
    def onClock(self, bohater):
        if self.in_action:
            try:
                if self.challenges[self.challenge_index].onClock(bohater):
                    bohater.applyReward(self.challenges[self.challenge_index].reward)
                    self.challenge_index += 1
                    if self.challenge_index != self.amount:
                        return False
                    bohater.applyReward(self.reward)
                    self.in_action = False
                    return True
            except CampException:
                raise  # do nadrzednej metody
#todo w nadrzednej metodzie - czy probujemy wykonac nastepne wyzwania w nadziei, ze starczy na nie atr pasywnych, czy pomijamy to?
            except Exception as e:
                print(e)
                print("ADVENTURE EXCEPTION")


if __name__ == "__main__":
    pass