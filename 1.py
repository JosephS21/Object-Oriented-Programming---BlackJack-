import random


class card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def cardvalue(self):
        if self.rank == "J" or self.rank == "Q" or self.rank == "K":
            return 10
        elif self.rank == "A":
            return 11
        else:
            return int(self.rank)

        

class Deck:
    def __init__(self):
        self.deck = []


    def createddeck(self):
        ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        suits = ["Spades ♠", "Clubs ♣", "Hearts ♥", "Diamonds ♦"]
        

        for i in suits:
            for x in ranks:
                cards = card(i,x)
                self.deck.append(cards)
        
        
    
    def shuffledeck(self):
        random.shuffle(self.deck)


    def printdeck(self):
        for i in self.deck:
            print(i.rank,i.suit)

    


class Dealer:
    def __init__(self, deck):
        self.deck = deck
        self.listofd = []
        self.listofp = []

    def deal(self):
        x=self.deck.pop()
        print(x.rank,x.suit)
        self.listofp.append(x)
    
    def dealerdeal(self):
        x =self.deck.pop()
        print(x.rank,x.suit)
        self.listofd.append(x)
        


    def dealercards(self):
        d1=self.deck.pop()
        d2=self.deck.pop()
        print(d1.rank, d1.suit)
        print(" <card hidden>")
        self.listofd.append(d1)
        self.listofd.append(d2)
    
    def playercards(self):
        p1 = self.deck.pop()
        p2= self.deck.pop()
        print(p1.rank, p1.suit)
        self.listofp.append(p1)
        print(p2.rank,p2.suit)
        self.listofp.append(p2)

    def under21(self):
 
        if self.sumofplayercards() > 21:
            return False
        else:
            return True

    def sumofplayercards(self):
        Sum = 0 

        for I in range(len(self.listofp)): 
            Sum = Sum  + (self.listofp[I].cardvalue())
        return Sum


    def sumofdealercards(self):
        Sum = 0 

        for I in range(len(self.listofd)): 
            Sum = Sum  + (self.listofd[I].cardvalue())
        return Sum

    def aces(self):
        x = False
        for a in range(len(self.listofp)):
            if self.listofp[a].rank == "A":
                self.listofp[a].rank = "1"
                x = True
        return x
    
                


    def hitstand(self):
            hit = input('Would you like to hit[h] or stand/stay[s]? [h/s] ').lower()
            if hit == 'h':
                self.deal()
                print("New total: ", self.sumofplayercards())
                if self.under21() == True:
                    self.hitstand()
                else:
                    if self.aces() == True:
                        
                        self.hitstand()
                    else:
                        print("Your total is:", self.sumofplayercards())

            elif hit == 's':
                print("Players total:", self.sumofplayercards())
                return

            else: 
                print('Please press a valid key!')
                self.hitstand()
        
        
    

    def dealerhitstand(self):
        if self.sumofplayercards() > 21:
            print('Dealer wins!')
            return
        if self.sumofdealercards() <17:
            print('Dealers draw: ')
            self.dealerdeal()
            self.dealerhitstand()
            
        else: 
            print("Dealers total:", self.sumofdealercards())
            return

    def blackjack(self):
        if self.sumofplayercards() ==21:
            print('Player Blackjack! You Won, nice hand!')
            return True
        elif self.sumofdealercards() ==21:
            print('Dealer Blackjack! Unlucky you lost!')
            return True
        else:
            return False
        

    def winnerwinner(self):
        if self.sumofplayercards() < 21 and self.sumofdealercards() < 21:
            if self.sumofplayercards() > self.sumofdealercards():
                print(f'Player wins! ')
            elif self.sumofplayercards() == self.sumofdealercards():
                print("Its a tie! Let's play a new game!")
            else:
                print('Dealer wins!')
        elif self.sumofplayercards() < 21 and self.sumofdealercards() > 21:
            print('Dealer Bust, You win!')
        elif self.sumofplayercards() > 21 and self.sumofdealercards() < 21:
            print("You Bust, you Lost!")





        
    

playagain = "Y".lower()
while playagain == "Y".lower():

    deck1= Deck()
    deck1.createddeck()
    deck1.shuffledeck()
    print("                ♠♣♥♦ WELCOME TO BLACKJACK! ♠♣♥♦")
    print("                          Lets Play!")
    print(
        "Game Rules:  Get 21 or as close as possible without going over!\n\
        Dealer hits until he/she reaches at least 17.\n\
        Aces count as 1 or 11."
    )
    dealer1 = Dealer(deck1.deck)
    print(f'These are the dealer cards: ')
    dealer1.dealercards()
    print(f'These are the player cards: ')
    dealer1.playercards()
    x=dealer1.blackjack()
    if x == False:
        dealer1.hitstand()
        dealer1.dealerhitstand()
    dealer1.winnerwinner()
    playagain = input('Type "Y" if you want to play again! ').lower()
    if playagain != 'y':
        print('Lets play again next time!')
        print('★ Game Over! ★')