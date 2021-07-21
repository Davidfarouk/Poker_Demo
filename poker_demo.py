from os import system
import random

def create_deck()-> list:
    deck=[]
    
    for i in range (1,14):
        deck.append(i)
        deck.append(i+0.1)
        deck.append(i+0.2)
        deck.append(i+0.3)
    
    return deck
class Player:
    
    def __init__(self):
        pass
        self.cards_in_hand=[]
    def Empty_hand(self):
        self.cards_in_hand=[]
        

    def Hit_Me(self,Deck):
        self.cards_in_hand.append(Deck[0])
        self.cards_in_hand.sort()
        Deck.pop(0)
    
    def Game_Statues(self):
        pairscount=0
        suitcount=0
        straightcount=1
        three_of_kind=False
        four_of_kind=False
        flush_count=1
        
        i=0
        while i in range(len(self.cards_in_hand)-1):
        
            if (self.cards_in_hand[i] *10) %10  == ((self.cards_in_hand[i+1] -1)*10) % 10:
                flush_count+=1
                
                

        
            if int(self.cards_in_hand[i])  == int(self.cards_in_hand[i+1])-1:
                straightcount+=1 
                

            if  i<2 and int(self.cards_in_hand[i])  == int(self.cards_in_hand[i+1]) and int(self.cards_in_hand[i])  == int(self.cards_in_hand[i+2]) and int(self.cards_in_hand[i])  == int(self.cards_in_hand[i+3]):
                four_of_kind=True
                three_of_kind=False
                i+=1

            if i<3 and int(self.cards_in_hand[i])  == int(self.cards_in_hand[i+1]) and int(self.cards_in_hand[i])  == int(self.cards_in_hand[i+2]):
                three_of_kind=True
                
                i+=1
           
            if int(self.cards_in_hand[i])  == int(self.cards_in_hand[i+1]):
                
                pairscount+=1
                i+=1
            i+=1
        
#       

        print("cards in hand: " + str(self.cards_in_hand))
        if pairscount!=0 and straightcount<5 and three_of_kind==0:
            print("pairs: "+str(pairscount))
        if three_of_kind==True and four_of_kind==False and pairscount<1:
            print("3 of a kind")
            print(pairscount)
        if straightcount==5 and flush_count<5:
            print("straigh")
        if four_of_kind==True:
            print("four of a kind")
        if three_of_kind==True and pairscount>0:
            print("Full House")
        if flush_count==5 :
            print("Flush")
        if flush_count==4 and straightcount==5:
            print("straight flush")
        

            


            



         
clear = lambda: system('clear')
clear()
players_list=[]
nop=input("Enter Number Of Players: ")
Deck=create_deck()
random.shuffle(Deck)
for P in range (int(nop)):
    players_list.append(Player())

i=1
numrounds=input("enter number of round but keep in mind that the deck is 52 cards: ")
for rounds in range (int(numrounds)):
    i=1
    print("Round Number : "+str(rounds))
    for p in players_list:
        print("game statues for player: "+str(i))
        p.Hit_Me(Deck)
        p.Hit_Me(Deck)
        p.Hit_Me(Deck)
        p.Hit_Me(Deck)
        p.Hit_Me(Deck)
        p.Game_Statues()
        p.Empty_hand()
        i+=1







        













        