wrs = '''Abroad	Casual	Around	Couple
Accept	Caught	Arrive	Course
Access	Centre	Artist	Covers
Across	Centum	Aspect	Create
Acting	Chance	Assess	Credit
Action	Change	Assist	Crisis
Active	Charge	Assume	Custom
Actual	Choice	Attack	Damage
Advice	Choose	Attend	Danger
Advise	Chosen	August	Dealer
Affect	Church	Author	Debate
Afford	Circle	Avenue	Decade
Afraid	Client	Backed	Decide
Agency	Closed	Barely	Defeat
Agenda	Closer	Battle	Defend
Almost	Coffee	Beauty	Define
Always	Column	Became	Degree
Amount	Combat	Become	Demand
Animal	Coming	Before	Depend
Annual	Common	Behalf	Deputy
Answer	Comply	Behind	Desert
Anyone	Copper	Belief	Design
Anyway	Corner	Belong	Desire
Appeal	Costly	Beaker	Detail
Appear	County	Better	Detect
Beyond	Budget	During	Device
Bishop	Burden	Easily	Differ
Border	Bureau	Eating	Dinner
Bottle	Button	Editor	Direct
Bottom	Camera	Effect	Doctor
Bought	Cancer	Effort	Dollar
Branch	Cactus	Eighth	Domain
Breath	Carbon	Either	Double
Bridge	Career	Eleven	Driven
Bright	Castle	Emerge	Driver'''


def animation(i):
    if i == 7:
        print('''
              |
              |
              |
              |
              |
              |____________
              ''')
    elif i == 6:
                print('''
              |-----------
              |
              |     O
              |
              |
              |____________
              ''')
    elif i == 5:
                print('''
              |-----------
              |
              |     O
              |    /
              |
              |____________
              ''')
    elif i == 4:
                print('''
              |-----------
              |
              |     O
              |    /|
              |
              |____________
              ''')
    elif i == 3:
                print('''
              |-----------
              |
              |     O
              |    /|\\
              |
              |____________
              ''')
    elif i == 2:
                print('''
              |-----------
              |
              |     O
              |    /|\\
              |    /
              |____________
              ''')
    elif i == 1:
                print('''
              |-----------
              |
              |     O
              |    /|\\
              |    / \\
              |____________
              ''')
    elif i == 0:
                print('''
              |-----------
              |     |
              |     O
              |    /|\\
              |    / \\
              |____________
              ''')


# Split the input string by tab
x = wrs.split("\t")

# Initialize an empty list to store results
arr = []

# Iterate over each element in the split list
for i in x:
    # Check if a newline character exists in the string
    if "\n" in i:
        # Split the string at the newline character and append both parts to the result list
        arr.extend(i.split("\n"))
    else:
        # If no newline character is found, just append the string
        arr.append(i)

# Sort the list
arr.sort()

# Print the sorted list
# print(arr)