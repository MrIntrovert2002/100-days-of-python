PLACEHOLDER = "[name]"

with open("./Input/Letters/starting_letter.txt") as f:
    contents = f.read()

with open("./Input/Names/invited_names.txt") as n:
    names = n.readlines()

for i in range(len(names)):
    names[i] = names[i].strip("\n")
    contents = contents.replace(PLACEHOLDER, names[i])
    with open(f"./Output/ReadyToSend/letter_for_{names[i]}.txt", "w") as s:
        s.write(contents)
    contents = contents.replace(names[i], PLACEHOLDER)