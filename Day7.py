import Day7_utlis
words = Day7_utlis.arr

print("Welcome to Hangman!")
print("Guess the given word = _ _ _ _ _ _. You have 8 chances.")

# Select a random word from the list of words
import random
key = random.choice(words)
key = key.lower()

# Split key letters in a list
key_split =[]
for x in key:
    key_split.append(x)

# Initialize variables
found = ["_", "_", "_", "_", "_", "_"]
chosen_letters = []
won = False
i = 8

while i>0:
    letter = input("Enter a letter:")

    # If the user retries the previously tried letter
    if letter in chosen_letters:
        print("Already chosen this letter previously.")
        Day7_utlis.animation(i)
        print(f"You have found {found}")
        print(f"You have {i} chances left.")
    
    # If the letter given by the user is present in the key-word, specify where the letter is present in the key-word.
    elif letter in key:
        Day7_utlis.animation(i)
        for a in range(0,6):
            if key_split[a] == letter:
                print(f"letter in key at {a+1}")
                found[a] = letter
                print(f"You have found {found}")
        print(f"You have {i} chances left.")
    
    # If the user does not guess the letter right, reduce the number of lives by 1
    else:
        i -= 1
        print(f"Wrong choice. You have {i} chances left.")
        Day7_utlis.animation(i)
        print(f"You have found {found}")

    chosen_letters.append(letter)     # Add the letter to the list of letters previously chosen by the user.
    
    # If the key-word is found, terminate the loop and declare the win.
    if found == key_split:
        won = True
        break
    print("\n")

# Print whether the user won or lost the game.
if won:
    print(f"You guessed the word '{key}'. You won!")
else:
    print(f"You didn't guess the word '{key}'. You lose!")
    