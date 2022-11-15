from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu1 = Menu()
CoffeeMaker1 = CoffeeMaker()
MoneyMachine1 = MoneyMachine()


def order():
    continue_ = True
    while continue_:
        CoffeeMaker1.report()
        MoneyMachine1.report()
        choice = input(f"\nWhat would you like? ({menu1.get_items()})\n")
        menu_item1 = menu1.find_drink(choice)

        is_possible = CoffeeMaker1.is_resource_sufficient(menu_item1)
        if is_possible:
            pass
        else:
            choice3 = input(f"\nWant to order again? Type 'yes' or 'off' to turn off the machine.\n")
            if choice3 == 'yes':
                order()
            else:
                break

        is_money_enough = MoneyMachine1.make_payment(menu_item1.cost)

        if is_money_enough:
            CoffeeMaker1.make_coffee(menu_item1)

        choice2 = input(f"\nWant to order again? Type 'yes' or 'off' to turn off the machine.\n")
        if choice2 == 'yes':
            pass
        else:
            continue_ = False


order()
