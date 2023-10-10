import sys
import random

# Set up the Constants
HEARTS = chr(9829)
DIAMONDS = chr(9830)
SPADES = chr(9824)
CLUBS = chr(9827)
BACKSIDE = 'backside'


def main():
    print(''' Rules: 
          Try to get as close to 21 without going over. 
          Kings, Queens, and Jacks are worth 10 points. 
          Aces are worth 1 or 11 points. Cards 2 through 10 are worth their face value. 
          (H)it to take another card. (S)tand to stop taking cards. 
          On your first play, you can (D)ouble down to increase your bet but must hit exactly one more time before standing. 
          In case of a tie, the bet is returned to the player. The dealer stops hitting at 17. ''')

    money = 5000
    while True:  # main game loop
        if money < 0:
            # check if the player has run out money.
            print("You're broke!")
            sys.exit()

        # let players to play one round
        print('Money: ', money)
        bet = getBet(money)

        # give dealer and player two cards from the deck
        deck = getDeck()
        playerHand = [deck.pop(), deck.pop()]
        dealerHand = [deck.pop(), deck.pop()]

        # handle player actions
        print('bet: ', bet)
        while True:  # keep looping until player stands or busts
            displayHands(playerHand, dealerHand, False)
            print()

            # if the player bust
            if getHandValue(playerHand) > 21:
                break

            # get the player's move (H / S / D)
            move = getMove(playerHand, money - bet)

            # handle player actions
            if move == 'D':
                additionalBet = getBet(min(bet, (money - bet)))
                bet += additionalBet
                print('Bet increased to {}.'.format(bet))
                print('Bet: ', bet)

            if move in ('H', 'D'):
                newCard = deck.pop()
                rank, suit = newCard
                print('You drew a {} of {}.'.format(rank, suit))
                playerHand.append(newCard)

                if getHandValue(playerHand) > 21:
                    continue

            if move in ('S', 'D'):
                break

            # dealer actions
            if getHandValue(playerHand) <= 21:
                while getHandValue(dealerHand) < 17:
                    print('Dealer hits...')
                    dealerHand.append(deck.pop())
                    displayCards(playerHand, dealerHand, False)

                    if getHandValue(dealerHand) > 21:
                        break
                    input('Press Enter to continue...')
                    print('\n\n')

            # show the final hands
            displayCards(playerHand, dealerHand, True)

            playerValue = getHandValue(playerHand)
            dealerValue = getHandValue(dealerHand)

            # game result
            if dealerValue > 21:
                print('Dealer busts! You won ${}.'.format(bet))
                money += bet
            elif (playerValue > 21) or (playerValue < dealerValue):
                print('You lost')
                money -= bet
            elif playerValue == dealerValue:
                print('TIE !. You bet money is returned to you.')

            input('Press Enter to continue...')
            print('\n\n')


# ask the players how much they want to bet for this round
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
        if 1 <= bet <= maxBet:
            return bet  # valid bet

# To return a tuple of 52 cards in rank and suit


def getDeck():
    deck = []
    for suit in (HEARTS, DIAMONDS, SPADES, CLUBS):
        for rank in range(2, 11):
            deck.append(str(rank), suit)  # add the numbered cards
        for rank in ('A', 'K', 'Q', 'J'):
            deck.append(rank, suit)              # add rest of the cards
    random.shuffle(deck)
    return deck


# def displayHands(playerHand, dealerHand, showDealerHand):


def getHandValue(cards):
    value = 0
    numberOfAces = 0

    # add the value for non ace cards
    for card in cards:
        rank = card[0]
        if rank == 'A':
            numberOfAces += 1
        elif rank in ('K', 'Q', 'J'):
            value += 10
        else:
            value += int(rank)

    # add the value for aces
    value += numberOfAces
    for i in range(numberOfAces):
        if value + 10 <= 21:
            value += 10

    return value


def displayHands(playerHand, dealerHand, showDealerHand):
    if showDealerHand:
        print('Dealer', getHandValue(dealerHand))
        displayCards(dealerHand)
    else:
        print('Dealer: ???')
        displayCards([BACKSIDE] + dealerHand[1:])

    print('Player:', getHandValue(playerHand))
    displayCards(playerHand)


def displayCards(cards):
    rows = ['', '', '', '']

    for i, card in enumerate(cards):
        rows[0] += ' __ '
        if card == BACKSIDE:
            rows[1] += '|## | '
            rows[2] += '|###| '
            rows[3] += '|_##| '
        else:
            rank, suit = card
            rows[1] += '|{} | '.format(rank.ljust(2))
            rows[2] += '| {} | '.format(suit)
            rows[3] += '|_{}| '.format(rank.rjust(2, '_'))

    for row in rows:
        print(row)


def getMove(playerHand, money):
    while True:
        moves = ['(H)it', '(S)tand']

        if len(playerHand) == 2 and money > 0:
            moves.append('(D)ouble down')

        movePromt = ', '.join(moves) + '> '
        move = input(movePromt).upper()
        if move in ('H', 'S'):
            return move
        if move == 'D':
            return move


if __name__ == '__main__':
    main()
