MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 2.0,
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
    },
    "mocha": {
        "ingredients": {
            "water": 230,
            "milk": 100,
            "coffee": 20,
        },
    "cost": 2.8
    },
}

profit = 0
machine_resources = {
    "water": 1000,
    "milk": 800,
    "coffee": 250,
}


def is_resource_sufficient(order_ingredients):
    """Function that takes drink ordered as parameter, return True if order can be made otherwise false"""
    is_enough = True
    for item in order_ingredients:
        if order_ingredients[item] > machine_resources[item]:
            print(f"Sorry, there is not enough of {item}")
            is_enough = False
    return is_enough


def process_payment():
    """Returns the total calculated from cash/coins inserted"""
    print("Please insert cash/coins: ")
    total = int(input("How many 1 dollar cash: "))
    total += int(input("How many 50 cents: ")) * 0.5
    total += int(input("How many 25 cents: ")) * 0.25
    total += int(input("How many 10 cents: ")) * 0.10
    return total


def is_transaction_successful(money_received, drink_cost):
    """Returns True if payment successful other False"""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Please find your change: ${change}")
        global profit
        profit += drink_cost    # profit is local scope here
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(drink_name, order_ingredients):
    """Deduct required drink ingredients from machines resources"""
    for item in order_ingredients:
        machine_resources[item] -= order_ingredients[item]
    print(f"Please enjoy your {drink_name}☕")

def add_resources():
    """Add resources into coffee machines"""
    global machine_resources
    machine_resources["water"] += int(input("How much water to add: "))
    machine_resources["milk"] += int(input("How much milk to add: "))
    machine_resources["coffee"] += int(input("How much coffee to add: "))
    print("Resources added successfully")


is_on = True

while is_on:
    choice = input("What would you like? Espresso/Latte/Cappuccino/Mocha: ").lower()
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {machine_resources['water']}")
        print(f"Milk: {machine_resources['milk']}")
        print(f"Coffee: {machine_resources['coffee']}")
        print(f"Money: {profit}")
    elif choice == "add":
        add_resources()
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_payment()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])

