from currency import *
from decimal import Decimal

class ActiveAttribute:
    #todo
    def __init__(self, nazwa, currency):
        self.name = nazwa
        self.exp_to_next_level = Decimal(50)
        self.level = Decimal(0)
        self.points = Decimal(0) #nazwa uzywana w klasie Adventure
        self.currency = currency

class PassiveAttribute:
    #todo
    def __init__(self, nazwa, max):
        self.name = nazwa
        self.exp_to_next_level = Decimal(50)
        self.level = Decimal(0)             #trzeba ten atrybut?
        self.max = Decimal(max)
        self.actual = Decimal(100)  #nazwa uzywana w klasie Adventure

    #def increaseMax(self, increment):
    #   self.max += increment
    

class Hero:
    def __init__(self,name):
        #nazwa
        self.name=name
        #waluty
        self.currency_might = Currency(0,'might_exp')
        self.currency_cunning = Currency(0,'cunning_exp')
        self.currency_psyche = Currency(0,'psyche_exp')
        self.currency_lore = Currency(0,'lore_exp')
        self.treasures = Currency(0,'treasure')
        self.riches = Currency(0,'gold')
        self.gold_to_spend=self.treasures + self.riches
        #atrybuty czynne
        self.might = ActiveAttribute('Might', self.currency_might)
        self.cunning = ActiveAttribute('Cunning', self.currency_cunning)
        self.psyche = ActiveAttribute('Psyche', self.currency_psyche)
        self.lore = ActiveAttribute('Lore', self.currency_lore)
        self.active = [self.might, self.cunning, self.psyche, self.lore]
        #atrybuty pasywne
        self.stamina = PassiveAttribute('Stamina',100)
        self.health = PassiveAttribute('Health',100)
        self.ploy = PassiveAttribute('Ploy',100)
        self.spirit = PassiveAttribute('Spirit',100)
        self.clarity = PassiveAttribute('Clarity',100)
        self.passive = [self.stamina, self.health, self.ploy, self.spirit, self.clarity]
        #umiejetnosci
        self.skills = None#jakies inne umiejetnosci czy chodzi o atrybuty czynne ? 
        #ekwipunek
        self.eq=Equipment(5)
        #zalozony ekwipunek
        self.weapon=None
        self.helmet=None
        self.armor=None
        self.ring=None
        #caly set ubrany
        self.set=[self.weapon,self.helmet,self.armor,self.ring]
        self.updateActiveAttributes()

    def getChallengeReward(self, challenge_reward):
        #otrzymanie nagrody za ukonczony challenge, nazwa metody taka?? uzyta w klasie Adventura
        pass

    def getAdventureReward(self, adventure_reward):
        pass
    
    #Zaktualizowanie statystyk o wartosci zalozonych przedmiotow
    def updateActiveAttributes(self):
        for i in self.set:
            if i != None:
                self.might.currency += i.item_might
                self.cunning.currency += i.item_cunning
                self.psyche.currency += i.item_psyche
                self.lore.currency += i.item_lore
    
    #Wyposazenie bohatera w przedmiot z naszego ekwipunku
    def setActiveItem(self,it):
        if it in self.eq.all_items:
            for i in range(len(it.min_attr)):
                if it.min_attr[i] > self.active[i].currency:
                    raise Exception('You have too few ' + self.active[i].name + ' points to wear this item')
        if it.type=='Weapon':
            self.weapon=it
            self.set[0]=it
        elif it.type=='Helmet':
            self.helmet=it
            self.set[1]=it
        elif it.type=='Armor':
            self.armor=it
            self.set[2]=it
        elif it.type=='Ring':
            self.ring=it
            self.set[3]=it
        else:
            raise Exception('Not supported type of item')
        self.updateActiveAttributes()
        
    def printHeroActive(self):
        print('Might :',self.might.currency)
        print('Cunning :',self.cunning.currency)
        print('Psyche :',self.psyche.currency)
        print('Lore :',self.lore.currency)
        
    def printHeroPassive(self):
        print('Stamina : ',self.stamina.actual)
        print('Health : ',self.health.actual)
        print('Ploy : ',self.ploy.actual)
        print('Spirit : ',self.spirit.actual)
        print('Clarity : ',self.clarity.actual)
            
    
class Item:
    
    def __init__(self,name,type,minimum=[0,0,0,0],m=0,c=0,p=0,l=0):
        self.name=name
        self.type=type
        
        #tablica minimalnych atrybutów aktywnych ktore musi miec bohater aby zalozyc przedmiot
        self.min_attr=[]
        for i in range(len(minimum)):
            self.min_attr.append(Decimal(minimum[i]))
        
        self.item_might=Currency(m,'attribute')
        self.item_cunning=Currency(c,'attribute')
        self.item_psyche=Currency(p,'attribute')
        self.item_lore=Currency(l,'attribute')
        self.item_attr=[self.item_might,self.item_cunning,self.item_psyche,self.item_lore]
    
    #Ustawienie minimalnych atrybutow potrzebnych do zalozenia przedmiotu
    def setMinAttr(self,new):
        for i in range(len(new)):
            self.min_attr[i]=Decimal(new[i])
    
    def printItem(self):
        print(self.name)
        print(self.type)
        print(self.min_attr)
        print('Might +',self.item_might)
        print('Cunning +',self.item_cunning)
        print('Psyche +',self.item_psyche)
        print('Lore +',self.item_lore)


class Equipment:
    
    def __init__(self,size):
        self.size=size
        self.all_items=[]
        self.weapons=[]
        self.helmets=[]
        self.armors=[]
        self.rings=[]
        
    #Dodaje przedmiot do ekwipunku
    def addItem(self,i):
        if self.getFreeSpace():
            if i.type == 'Weapon':
                    self.weapons.append(i)
            elif i.type == 'Helmet':
                    self.helmets.append(i)
            elif i.type == 'Armor':
                    self.armors.append(i)
            elif i.type == 'Ring':
                    self.rings.append(i)
            else:
                raise Exception('Not supported type of item')
            self.all_items.append(i)

    #Oblicza ilosc wolnego miejsca w ekwipunku
    def getFreeSpace(self):
        if self.size - len(self.all_items) > 0:
            return True
        else:
            raise Exception('Too many items in equipment')
    
    #Jesli jest w eq przedmiot o danej nazwie, usuwa go z listy konkretnych przedmiotow oraz z ogolnej listy
    def removeItem(self,it):
        tmp_list=self.all_items.copy()
        for i in tmp_list:
            if i.name == it:
                if i.type == 'Weapon':
                    self.weapons.remove(i)
                elif i.type == 'Helmet':
                    self.helmets.remove(i)
                elif i.type == 'Armor':
                    self.armors.remove(i)
                elif i.type == 'Ring':
                    self.rings.remove(i)
                self.all_items.remove(i)
    
    
if __name__ == '__main__':
    
    print('UWAGA TESTY')
    h1 = Hero('Andrzej')
    print('Oto ',h1.name)
    print('')
    i1=Item('Dziadek do orzechow','Weapon')
    i1.setMinAttr([1,2,1,1])
    i1.item_might=2
    i1.item_cunning=3
    i1.item_psyche=0
    i1.item_lore=6
    i1.printItem()
    print('')
    i2=Item('Durszlak Spaczenia','Helmet')
    i2.setMinAttr([11,112,23,4])
    i2.item_might=5
    i2.item_cunning=13
    i2.item_psyche=8
    i2.item_lore=0
    i2.printItem()
    print('')
    
    h1.eq.addItem(i1)
    h1.eq.addItem(i2)
    print(h1.eq.weapons)
    print(h1.eq.helmets)
    print(h1.eq.armors)
    print(h1.eq.rings)
    #h1.eq.addItem(i1)
    #h1.eq.addItem(i1)
    #h1.eq.addItem(i1)
    #h1.eq.addItem(i1)
    print('Wiecej przedmiotow nie wejdzie do eq niz jest w nim miejsca')
    print('')
    print('Rozdaje postaci jakies poczatkowe punkty umiejetnosci')
    h1.might.currency+=10
    h1.cunning.currency+=10
    h1.psyche.currency+=10
    h1.lore.currency+=10
    
    h1.printHeroActive()    
    print('')
    print(h1.eq.all_items)
    print('Jeszcze w secie nic nie ma zalozonego')
    print(h1.set[0])
    h1.setActiveItem(i1)
    print('A teraz juz ma ')
    print(h1.set[0])
    print('')
    print('Zwiekszyly sie statystyki naszego bohatera')
    h1.printHeroActive()
    print('')
    h1.printHeroPassive()
    print('A to ponizej nie zadziala bo nasz bohater nie ma wystarczajacej ilosci punktow')
    #h1.setActiveItem(i2)
    
    '''
    for i in h1.active:
        print(i.currency)
        
    for i in h1.set:
        print(i)
        
    for i in h1.passive:
        print(i.actual)
    '''
    
    
    