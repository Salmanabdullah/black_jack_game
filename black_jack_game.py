import sys, random

# Set up the Constants
HEARTS = chr(9829)
DIAMONDS = chr(9830)
SPADES = chr(9824)
CLUBS = chr(9827)

def main():
    print(''' Rules: 
          Try to get as close to 21 without going over. 
          Kings, Queens, and Jacks are worth 10 points. 
          Aces are worth 1 or 11 points. Cards 2 through 10 are worth their face value. 
          (H)it to take another card. (S)tand to stop taking cards. 
          On your first play, you can (D)ouble down to increase your bet but must hit exactly one more time before standing. 
          In case of a tie, the bet is returned to the player. The dealer stops hitting at 17. ''')
    
    money = 5000
    while True:                 #main game loop
        if money <0:
            # check if the player has run out money.
            print("You're broke!")
            sys.exit()

        # let players to play one round
        print('Money: ',money)
        bet = getBet(money)


#ask the players how much they want to bet for this round
def getBet(maxBet):
    while True:         # keep asking until they enter a valid amount
        print('How much do you wanna bet? (1-{}, or QUIT)'.format(maxBet))
        bet = input('> ').upper().strip()
        if bet == 'QUIT':
            print('Thanks for Playing')
            sys.exit()

        if not bet.isdecimal():
            continue            # ask again if player didn't enter a number

        bet = int(bet)
        if 1<= bet <=maxBet:
            return bet          #valid bet







if __name__ == '__main__':
    main()
