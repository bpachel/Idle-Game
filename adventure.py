from hero import Hero, Item
from data_types import Currency
from decimal import Decimal
import random

class CurrencyContainer:
    def __init__(self, dif_level, forclass):
        # todo generowanie treasures
        temp = ['might_exp', 'cunning_exp', 'psyche_exp', 'lore_exp']

        if forclass == 'Challenge':
            self.exp = [Currency(Decimal(random.randrange(100,300,1)/100)*dif_level[i], i) for i in range(4)]
            self.gold = Currency(Decimal(random.randrange(200,500,1)/100)*sum(dif_level), 'gold')
            self.treasures = Currency(0,'treasure')

        #nagrody 3-5 razy wieksze niz w challenge
        if forclass == 'Adventure':
            self.exp = [Currency(Decimal(random.randrange(300,1500,1)/100)*dif_level[i], i) for i in range(4)]
            self.gold = Currency(Decimal(random.randrange(600,2500,1)/100)*sum(dif_level), 'gold')
            self.treasures = Currency(0,'treasure')

        #interfejs wypisuje tylko niezerowe nagrody
        self.print_list = [i for i in self.exp if i.val > Decimal(0)]
        if self.gold.val > Decimal(0):
            self.print_list.append(self.gold)
        if self.treasures.val > Decimal(0):
            self.print_list.append(self.treasures)

    pass

class ItemContainer:
    #przechowywanie itemow do zdobycia i losowanie ich na nagrode
    #wywolanie ItemContainer(dif_level, 'challenge')
    #self.waluta = ItemContainer(dif_level, 'adventure')
    #dif_level [0,0,0,0]
    pass



class Reward:
    #generowanie i przechowywanie nagrody za adventure/challenge
    def __init__(self, diff_level, type):
        self.waluta = CurrencyContainer(diff_level, type)
        self.eq = ItemContainer(diff_level, type)


#todo ustawienie parametrów losowania oraz
# aktualizacja wraz z postepem gry (coraz wyzsze przedzialy losowania)
# i generowanie coraz lepszych przedmiotow - tutaj czy w klasie Item????? - Lukasz wie

challenge_names = ["Wyzwanie1", "Walka z niedzwiedziem", "Przeplyniecie rzeki"]
adventure_names = ["Przygoda1", "Wyprawa w gory"]

class ObozException(Exception):
    pass

class Challenge: #wyzwanie
    def __init__(self, dif_level):
        self.name = random.choice(challenge_names);
        self.difficulty = [Decimal(random.randrange(50, 150, 1)/100)*dif_level[i] for i in range(4)]
        self.reward = Reward(self.difficulty, 'Challenge')
        #self.type = type            #[False,False,False,False]
        self.cost = [Decimal(random.randrange(50, 100, 1)/500)*self.difficulty[i] for i in range(4)]

    def onClock(self, bohater):
        temp_list = [bohater.passive[i].actual - self.cost[i] for i in range(4)]
        for i in temp_list:
            if i<=0:
                raise ObozException
        self.difficulty = temp_list
        for i in range(4):
            if self.difficulty[i] - bohater.active[i].points > 0:
                self.difficulty[i] -= bohater.active[i].points
            else: self.difficulty[i] = 0
        return self.difficulty == [0,0,0,0] #true if completed challenge
        #todo zwracanie nagrody

class Adventure: #przygoda
    def __init__(self, diff_level):
        self.name = random.choice(adventure_names)
        self.amount = random.randint(4,20)
        self.challenges = [Challenge(diff_level) for i in range(self.amount)]
        self.challenge_index = 0
        self.in_action = False
        self.reward = Reward(diff_level, 'Adventure')
        #todo pasek postepu przygody - gdzie? czy rzeba dodatkowe parametry initial_cost, initial_difficulty?
        #todo pasek postepu danego wyzwania - gdzie?

    def start(self):
        self.in_action = True


    # '''Zwraca bool czy bohater moze kontynuowac przygode.'''
    '''Zwraca bool czy przygoda zostala ukonczona.'''
    def onClock(self, bohater):
        if self.in_action:
            try:
                if self.challenges[self.challenge_index].onClock(bohater):
                    bohater.getChallengeReward(self.challenges[self.challenge_index].reward)
                    if self.challenge_index + 1 == self.amount:
                        self.challenge_index += 1
                        return False
                    else:
                        bohater.applyReward(self.reward)
                        self.in_action = False
                        return True
            except ObozException:
                raise #do nadrzednej metody
            except Exception as e:
                print(e)
                print("ADVENTURE EXCEPTION")
        #todo zwracanie nagrody






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

if __name__ == "__main__":
    pass