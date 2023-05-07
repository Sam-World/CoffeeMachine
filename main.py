MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
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
    "money": 0,
}


# TODO: 2. turn off the coffee machine by entering "off" to the prompt

def resources_report():
    """values of resources"""
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]
    money = resources["money"]


# TODO: 3. print report
def print_report():
    """print a formatted report of resources"""
    for key, value in resources.items():
        if key == "coffee":
            print(f"{key} : {value}g")
        elif key == "money":
            print(f"{key} : ${value}")
        else:
            print(f"{key} : {value}ml")


# TODO: 4. check resources sufficient?
def resources_check(drink_choice):
    """compare resources against drink ingredients"""
    for x in MENU[drink_choice]["ingredients"]:
        if int(MENU[drink_choice]["ingredients"].get(x)) > int(resources.get(x)):
            print(f"Sorry there is not enough {x}")
            return "resources_out"

def update_resources():
    """update resources list after transaction"""
    for y in MENU[drink_choice]["ingredients"]:
        new_value = int(resources.get(y)) - int(MENU[drink_choice]["ingredients"].get(y))
        resources[y] = new_value
    money = float(resources["money"])
    cost = float(MENU[drink_choice]["cost"])
    updated_money = money + cost
    resources.update(money = updated_money)


# TODO: 6. check transaction successful?
def check_transaction(tot_coins_ins):
    """check if the user has inserted enough money, give change, make drink"""
    if tot_coins_ins < MENU[drink_choice]['cost']:
        print("You haven't inserted enough money, here is your money back.")
    else:
        change_given = float(tot_coins_ins) - float(MENU[drink_choice]['cost'])
        change = round(change_given, 2)
        print(f"Your change is ${change}")
        print(f"Here is you {drink_choice}, enjoy!")
        update_resources()


coffee_machine_on = True
while coffee_machine_on:

    # TODO: 1. prompt user by asking "what would you like? (espresso/latte/cappuccino):"
    drink_choice = input("\nWhat would you like? (espresso/latte/cappuccino): ").lower()

    if drink_choice == "report":
        print_report()
        drink_choice = input("\nWhat would you like? (espresso/latte/cappuccino): ").lower()
    if drink_choice == "off":
        exit("Exit")
    if drink_choice == "espresso" or "latte" or "cappuccino":
        if resources_check(drink_choice) != "resources_out":


            # TODO: 5. process coins

            print(f"A {drink_choice} costs ${MENU[drink_choice]['cost']}\n")

            quarters = float(input("How many quarters?: ")) * 0.25
            dimes = float(input("How many dimes?: ")) * 0.1
            nickles = float(input("How many nickles?: ")) * 0.05
            pennies = float(input("How many pennies?: ")) * .01

            total_coins_inserted = quarters + dimes + nickles + pennies
            tot_coins_ins = round(total_coins_inserted, 2)
            print(f"You have inserted ${tot_coins_ins}")

            check_transaction(tot_coins_ins)
        elif int(resources.get("water")) < 50:
            coffee_machine_on = False

# TODO: 7. make coffee