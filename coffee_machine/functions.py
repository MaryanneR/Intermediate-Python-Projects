import sys
import resources as r
import menu as m
import coins as c
import os


def clear():
    """
    Clears console
    """
    os.system('cls')


def what_order():
    """
    Gets order from customer, allowing them to choose only valid options from the menu.
    Also allows for machine settings to be accessed. 'off' will shut off the machine.
    :return: order value, unless input is 'off' in which case, the machine shuts down
    """
    order = input("\nWhat would you like to order? Type 'e' for espresso, 'l' for latte, or 'c' for cappuccino: ").lower()
    while order not in ('e', 'l', 'c', 's', 'off'):
        order = input("\nPlease enter either 'e', 'l', or 'c' to order coffee, or 's' to access machine settings: ").lower()
    if order in ('e', 'l', 'c'):
        if order == 'e':
            order = 'espresso'
            article = 'an'
        elif order == 'l':
            order = 'latte'
            article = 'a'
        else:
            order = 'cappuccino'
            article = 'a'
        print(f"\nYou have ordered {article} '{order}'")
        return order
    elif order == 's':
        print("\nYou have chosen to access the machine settings...\n")
        machine_settings(order)
        return order
    else:
        sys.exit("Shutting down....")


def machine_settings(order):
    """
    Allows access to machine settings. Customer can either print a list of current machine resources or
    choose to add resources to the machine. Can also choose to shut off machine.
    :param order: customer input from what_order()
    """
    action = input("Would you like to print a report or add resources to machine?\nType 'r' for report or 'a' to "
                   "add: ").lower()
    while action not in ('r', 'a', 'off'):
        action = input("Please enter either 'r' or 'a': ").lower()
    if action == 'r':
        print("\nCurrent machine resources: ")
        print(r.resources)
        print("Machine has collected: ${:.2f}".format(r.earnings))
    elif action == 'a':
        print("\nYou have chosen to add resources to the machine")
        add_resources()
    else:
        sys.exit("Shutting down....")


def running_low():
    """
    Prints alert message if machine resources are running low
    """
    low_message = ''
    if r.resources['water'] <= 250:
        low_message += 'Water'
    if r.resources['milk'] <= 150:
        if low_message == '':
            low_message += 'Milk'
        else:
            low_message += ', Milk'
    if r.resources['coffee'] <= 24:
        if low_message == '':
            low_message += 'Coffee'
        else:
            low_message += ', Coffee'
    if len(low_message) > 6:
        verb = 'are'
    else:
        verb = 'is'
    if low_message != '':
        print(f"***{low_message} {verb} running low. Please restock***")


def add_resources():
    """
    Allows user to add resources to the machine. Does not allow resource amount to exceed MAX_AMOUNTS
    """
    to_add = input("\nWhat resource would you like to add? Water, milk, or coffee?: ").lower()
    while to_add not in ('water', 'milk', 'coffee', 'off'):
        to_add = input("Please enter either 'water', 'milk', 'coffee': ").lower()
    if to_add == 'off':
        sys.exit("Shutting down....")
    if to_add in ('water', 'milk'):
        measurement = 'mL'
    else:
        measurement = 'g'
    old_amount = r.resources[to_add]
    if old_amount == r.MAX_AMOUNTS[to_add]:
        print(f"There is already enough {to_add} in the machine.")
        add_resources()
    print(f"There is currently {old_amount} {measurement} of {to_add} in the machine.")
    add_amount = int(input(f"How much {to_add} would you like to add to the machine?: "))
    while (old_amount + add_amount) > r.MAX_AMOUNTS[to_add]:
        print(f"The machine can only hold {r.MAX_AMOUNTS[to_add]} {measurement}of {to_add}\nThere is currently "
              f"{old_amount} {measurement} of {to_add} in the machine")
        add_amount = int(input(f"Please enter a smaller amount of {to_add}: "))
    new_amount = old_amount + add_amount
    r.resources[to_add] = new_amount
    print(f"New resources amount: {r.resources}")
    more_to_add = input("Do you have any other resources to add to the machine? Type 'y' or 'n': ").lower()
    while more_to_add not in ('y', 'n'):
        more_to_add = input("Please enter 'y' or 'n': ").lower()
    if more_to_add == 'y':
        add_resources()
    else:
        clear()
        return


def sufficient_resources(order):
    """
    Checks if machine has sufficient resources to make order
    Prints different message depending on whether there are sufficient resources or not
    :param order: input from customer (excludes 's' input)
    :return: Boolean value
    """
    can_brew = True
    need_more = []
    for item, amount in m.MENU[order]['ingredients'].items():
        if amount > r.resources[item]:
            need_more.append(item)
            can_brew = False
        else:
            r.resources[item] -= amount
    if not can_brew:
        print(f"Sorry, there is not enough {need_more} for this order")
    else:
        print("Your coffee will start brewing once payment has been made")
    return can_brew


def another_order():
    """
    Asks customer if they would like to order again
    :return: if `another` == 'y' then `another` is returned, if not then the machine shuts down
    """
    another = input("Would you like to order something else? Type 'y' or 'n': ").lower()
    while another not in ('y', 'n'):
        another = input("Please enter either 'y' or 'n': ").lower()
    if another == 'y':
        return another
    else:
        sys.exit("Shutting down....")


def payment(order):
    """
    Gets price of order item, collects coins from customer, and evaluates coin amount
    If coin amount is not sufficient, machine refunds coins to customer and prints an informative message
    If coin amount is sufficient or overly sufficient, print explanatory message and refund change if necessary
    Coins for successful payments are added to the machine's `earnings` tally.
    :param order: customer input
    """
    # Get cost of menu item
    price = m.MENU[order]['cost']
    print("The price is ${:.2f}".format(price))
    print("\nThis machine only takes coins\nPlease enter your coins now")
    # Get coins from player
    quarters = int(input("How many quarters do you have?: ")) * c.COINS['quarter']
    dimes = int(input("How many dimes do you have?: ")) * c.COINS['dime']
    nickels = int(input("How many nickels do you have?: ")) * c.COINS['nickel']
    pennies = int(input("How many pennies do you have?: ")) * c.COINS['penny']
    total = quarters + dimes + nickels + pennies
    if price > total:
        print("Sorry, that's not enough money. Refunding ${:.2f}".format(total))
    elif price < total:
        change = total - price
        r.earnings += price
        print("Your change is ${:.2f}\nPlease stand by for your coffee".format(change))
    else:
        r.earnings += price
        print("Thanks for the exact change!\nPlease stand by for your coffee")
