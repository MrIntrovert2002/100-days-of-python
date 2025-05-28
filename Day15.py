print('Coffee Machine Program!☕')

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
profit = 0

def check_resources(drink, res):
    """ Checks availability of resources. Reurns boolean value. """
    def check(t):
        if res[t] >= MENU[drink]['ingredients'][t]:
            return True
        return False
    if check('water') & check('milk') & check('coffee'):
        return True
    else:
        if not check('water'):
            print("Sorry we don't have enough water.")
        elif not check('milk'):
            print("Sorry we don't have enough milk.")
        elif not check('coffee'):
            print("Sorry we don't have enough coffee.")
    return False

def check_coins(drink):
    """ Cunducts the transaction for money. Returns boolean value. """
    price  = MENU[drink]['cost']
    print(f"Sure! Please insert ${price} in coins.")
    curr = { "quarters": 0.25, "dimes": 0.10, "nickles": 0.05, "pennies": 0.01 }
    total_in = 0
    for i in curr:
        total_in += int(input(f"How many {i}?: "))*curr[i]
    if total_in < price:
        print("Sorry that's not enough money. Money refunded!")
        return False
    else:
        print(f"Here is your ${total_in-price} change!")
        return True

def make_coffee(drink, res, p):
    """ Deducts the resources required for the coffee. Updates resources and money. """
    def add_in(t):
        res[t] -= MENU[drink]['ingredients'][t]
    add_in('water'), add_in('milk'), add_in('coffee')
    p += MENU[drink]['cost']
    print(f"Here is your {drink} ☕ Enjoy!")
    return res, p

while True:
    print('\nWelcome!!')
    user_prompt = input('What would you like? (espresso/latte/cappuccino): ')
    if user_prompt == 'off':
        print('Turning Off...')
        break
    elif user_prompt == 'report':
        print(f"The current resources are:\n Water: {resources['water']}ml\n Milk: {resources['milk']}ml\n Coffee: {resources['coffee']}\n Money: ${profit}")
        continue
    elif user_prompt in MENU:
        if check_resources(user_prompt, resources):
            if check_coins(user_prompt):
                resources, profit = make_coffee(user_prompt, resources, profit)
            else:
                continue
        else:
            continue
    else:
        print("Wrong Input!!\nPlease try again.\n")
        continue
