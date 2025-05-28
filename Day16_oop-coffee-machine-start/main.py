from menu import Menu
# from menu import MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

print('Coffee Machine Program!☕')

coffee_machine = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()
# a = 'latte'
# print(menu.find_drink(a).ingredients)
# coffee_machine.report()
# money_machine.report()


while True:
    print('\nWelcome!!')
    user_prompt = input(f"What would you like? ({menu.get_items()}): ")
    if user_prompt == 'off':
        print('Turning Off...')
        break
    elif user_prompt == 'report':
        coffee_machine.report()
        money_machine.report()
    elif coffee_machine.is_resource_sufficient(menu.find_drink(user_prompt)):
        item = menu.find_drink(user_prompt)
        print(f"Sure! Your total is ${item.cost}.")
        if money_machine.make_payment(item.cost):
            coffee_machine.make_coffee(item)
    else:
        print("Please try again.\n")
        continue