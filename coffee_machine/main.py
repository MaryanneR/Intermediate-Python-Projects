import functions as f


def coffee_machine():
    # Greeting
    greeting = "\n☕ HOT COFFEE ☕\nEspresso: $1.50\nLatte: $2.50\nCappuccino: $3.00\n"
    print(greeting)
    f.running_low()
    can_brew = True

    while can_brew:
        # Get order
        order = f.what_order()
        if order == 's':
            coffee_machine()
        # Check if enough resources for order
        can_brew = f.sufficient_resources(order)
        # If enough resources, ask for payment
        if can_brew:
            f.payment(order)
            print("Enjoy your coffee!")
        # Ask if they would like to order anything else
        another = f.another_order()
        if another == 'y':
            f.clear()
            coffee_machine()


coffee_machine()
