from decimal import getcontext, Decimal
import random

class RewardChallenge:
    def __init__(self, attr, eq):
        self.attr = attr    #[0,0,0,0]
        self.eq = eq        #lista obiektow Item


# todo - jakiego rodzaju nagrody za cala przygode?
class RewardAdventure:
    def __init__(self):
        pass

#Lukasz - parametry Challenge generujemy losowo.

# todo wewnatrz klasy challenge czy poza nia i gotowe obiekty przekazac przez argumenty?

#todo ustawienie parametrów losowania oraz
# aktualizacja wraz z postepem gry (coraz wyzsze przedzialy losowania)
# i generowanie coraz lepszych przedmiotow - tutaj czy w klasie Item?????
class Challenge: #wyzwanie
    def __init__(self, reward, type, dif_level, cost):
        self.reward = reward        #obiekt typu RewardChallenge?
        self.type = type            #[False,False,False,False]
        self.difficulty = dif_level #[0,0,0,0]
        self.cost = cost            #[0,0,0,0]

class Adventure: #przygoda
    def __init__(self, reward, dif_level, cost):
        self.amount = random.randint(4,20)
        self.challenges = [Challenge() for i in range(self.amount)]
        self.in_action = False
        self.reward = reward     #obiektRewardAdventure
        #pasek postepu przygody - gdzie?
        #pasek postepu danego wyzwania - gdzie?

class Item:
    def __init__(self):
        pass



"""
Work, Act

Trening postaci odbywa się za pomocą akcji typu Work i Act z karty Main. 
Trening odbywa się dwufazowo.

	Pierwsza faza - niektóre akcje Work i Act zdobywają punkty doświadczenia
	 po każdym użyciu. Doświadczenie to jest reprezentowane jako procentowa
	  miara do następnego poziomu. Każde wykonanie akcji zwiększa ją 
	  o2%, 4% lub 10% w zależności od złożoności czynności. 
	  Gdy miara dojdzie do 100%, akcja wchodzi na nowy poziom, 
	  z wyzerowaną miarą postępu.
	  
	Faza druga - część akcji Work i Act generują waluty doświadczenia, 
	które można wykorzystać do aktywowania akcji upgrade zwiększających 
	atrybuty postaci lub na zakup umiejętności postaci z karty Skills.

"""

class Work:
    def __init__(self):
        #wg specyfikacji przygoda blokuje wszystkie akcje work
        pass

class Act:
    def __init__(self, block_on_adventure = True):
        self.block_on_adventure = block_on_adventure
        pass





class ActiveAttribute:
    def __init__(self, nazwa, currency):
        self.name = nazwa
        self.exp_to_next_level = Decimal(0)
        self.level = Decimal(0)
        self.points = Decimal(0)
        self.currency = Currency(currency)

class PassiveAttribute:
    def __init__(self, nazwa, max):
        self.name = nazwa
        self.exp_to_next_level = Decimal(50)
        self.level = Decimal(0)             #trzeba ten atrybut?
        self.max = Decimal(max)
        self.actual = Decimal(max)

    #def increase_max(self, increment):
    #    self.max += increment



class Currency:
    def __init__(self, amount=0):
        self.set = Decimal(amount)

class Bohater:
    def __init__(self):
        #waluty
        self.currency_might = Currency(0)
        self.currency_cunning = Currency(0)
        self.currency_psyche = Currency(0)
        self.currency_lore = Currency(0)
        self.treasures = Currency(0)
        self.riches = Currency(0)
        #atrybuty czynne
        self.might = ActiveAttribute('Might', self.currency_might)
        self.cunning = ActiveAttribute('Cunning', self.currency_cunning)
        self.psyche = ActiveAttribute('Psyche', self.currency_psyche)
        self.lore = ActiveAttribute('Lore', self.currency_lore)
        #atrybuty pasywne
        self.stamina = PassiveAttribute('Stamina')
        self.health = PassiveAttribute('Health')
        self.ploy = PassiveAttribute('Ploy')
        self.spirit = PassiveAttribute('Spirit')
        self.clarity = PassiveAttribute('Clarity')
        self.passive = [self.might, self.cunning, self.psyche, self.lore]
        self.active = [self.stamina, self.health, self.ploy, self.spirit, self.clarity]




def main():


if __name__ == "__main__":
    main()