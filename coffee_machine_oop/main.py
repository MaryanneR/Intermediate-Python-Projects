from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()
machine_on = True

while machine_on:
    greeting = "\n☕ HOT COFFEE ☕\nEspresso: $1.50\nLatte: $2.50\nCappuccino: $3.00\n"
    print(greeting)
    menu_options = menu.get_items()
    order = input(f"What would you like to order? ({menu_options}): ").lower()
    if order == "off":
        machine_on = False
    elif order == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink_to_make = menu.find_drink(order)
        if coffee_maker.is_resource_sufficient(drink_to_make) and money_machine.make_payment(drink_to_make.cost):
            coffee_maker.make_coffee(drink_to_make)
