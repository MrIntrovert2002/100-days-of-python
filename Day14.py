print("Welcome to the Higher or Lower Game!!")
from Day14_data import data
import random
score = 0
game_lost = False
# print(data)

def choose():
    return random.choice(data)

# A_data = choose()
# print(f"Compare A: {A_data['name']}, a {A_data['description']}, from {A_data['country']}.")

A_data = choose()
while game_lost == False:
    print(f"Compare A: {A_data['name']}, a {A_data['description']}, from {A_data['country']}.")
    B_data = choose()
    while A_data == B_data:
        B_data = choose()
    
    print(f"Against B: {B_data['name']}, a {B_data['description']}, from {B_data['country']}.")
    choice = input("Who has more followers? Type 'A' or 'B': ").upper()

    if A_data['follower_count'] > B_data['follower_count']:
        if choice == "A":
            score+=1
        elif choice == "B":
            print(f"You guessed wrong. Your total score is {score}.")
            game_lost = True
            break
        else:
            print("Wrong input! Plsease type 'A' or 'B'.")
            continue

    if A_data['follower_count'] < B_data['follower_count']:
        if choice == "B":
            score+=1
        elif choice == "A":
            print(f"\nYou guessed wrong. Your total score is {score}.")
            game_lost = True
            break
        else:
            print("Wrong input!")
            continue

    if game_lost == True:
        break
    else:
        print(f"\nYou guessed correct! Your score is {score}.\n\n")
        A_data = B_data
        continue



