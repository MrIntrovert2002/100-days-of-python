from random import randint
print("Welcome to the number guessing game!")
rand_num = randint(1,100)
# print(rand_num)
def compare():
    guess = int(input("Make a guess: "))
    if guess == rand_num:
        return True
    elif guess > rand_num:
        print("Too high.")
        return False
    else:
        print("Too low.")
        return False

print("I'm thinking of a number between 1 and 100.")
diff = input("choose a difficulty. Type 'easy' or 'hard': ")

if diff == 'easy':
    attempts = 10
else:
    attempts = 5
ans = False
while attempts > 0:
    print(f"You have {attempts} attempts remaining to guess the number.")
    ans = compare()
    if ans == True:
        break
    attempts -= 1
if ans == True:
    print("You guessed the right number. You Won!!")
else:
    print("You are out of attempts. You lost!")