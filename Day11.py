import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
print("Welcome to BlackJack!")
dealer_cards = []
player_cards = []

dealer_cards.append(random.choice(cards))
player_cards.append(random.choice(cards))
print(f"One of dealer's drawn cards is {dealer_cards}.")

dealer_sum = 0
while dealer_sum<17:
    dealer_sum = 0
    dealer_cards.append(random.choice(cards))
    j=0
    for i in dealer_cards:
        dealer_sum += i
        if i==11:
            j+=1
    while dealer_sum > 21 and j>0:
        dealer_sum -= 10
        j-=1


choice = "y"
player_sum = 0
while player_sum < 21 and choice == "y":
    player_sum = 0
    player_cards.append(random.choice(cards))
    print(f"You have drawn cards {player_cards}.")
    j=0
    for i in player_cards:
        player_sum += i
        if i==11:
            j+=1
    if player_sum > 21 and j>0:
        player_sum -= 10
        j-=1

    print(f"Your sum is {player_sum} and you cards are {player_cards}")
    if player_sum > 21:
        break
    choice = input("Would you like to draw another card?")

if dealer_sum > 21:
    print(f"Dealer's sum is {dealer_sum} so you win by default.")
elif player_sum > 21:
    print("Its a bust. You lost!")
elif player_sum == dealer_sum:
    print(f"Its a tie. Both of your sum is {player_sum}.")
elif player_sum > dealer_sum:
    print(f"You Won. You have a sum of {player_sum} and dealer has a sum of {dealer_sum}.")
else:
    print(f"You Lose. You have a sum of {player_sum} and dealer has a sum of {dealer_sum}.")

print(f"Player cards: {player_cards}\nDealer cards: {dealer_cards}")