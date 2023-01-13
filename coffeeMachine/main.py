# TODO: 1. Create Menu
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

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


# TODO: 2. Print report
def print_report(resources, profit):
    print(f"Water: {resources['water']}")
    print(f"Milk: {resources['milk']}")
    print(f"Coffee: {resources['coffee']}")
    print(f"Profit: ${profit}")


# TODO: 3. Get order resources
def get_resources(order):
    for key in MENU:
        if key == order:
            return MENU[key]["ingredients"]


# TODO: 4. Check resources
def check_resources(resources,order_resources):
    for key in order_resources:
        if key in resources:
            if resources[key] < order_resources[key]:
                print(f"Sorry there is not enough {key}")
                return False
    return True


# TODO:  5. Process Coins
def payment_process(order_status, order):
    if order_status == True:
        print("Please insert coins")
        q = int(input("How many quarters? "))
        d = int(input("How many dimes? "))
        n = int(input("How many nickles? "))
        p = int(input("How many pennies? "))
        payment = 0.25*q + 0.1*d + 0.05*n + 0.01*p
        if payment < float(MENU[order]["cost"]):
            print("Sorry that's not enough money. Money refunded ")
            return False
        else:
            change = round(payment - float(MENU[order]["cost"]),1)
            print(f"Here is ${change} in change")
            return True


#TODO: 6. Make coffee
def make_coffee(order_status, payment_status, order, order_resources, resources,profit):
    if order_status and payment_status == True:
        profit += float(MENU[order]["cost"])
        for key in order_resources:
            if key in resources:
                resources[key] -= order_resources[key]
        print(f"Here is your {order}. Enjoy!")


def coffee_machine(resources, profit):
    is_on = True
    while(is_on):
        order = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if order == "off":
            is_on = False
        elif order == "report":
            print_report(resources, profit)
        else:
            order_resources = get_resources(order)
        # print(order_resources)
            order_status = check_resources(resources, order_resources)
        # print(order_status)
            payment_status = payment_process(order_status, order)
        # print(payment_status)
            make_coffee(order_status, payment_status, order, order_resources, resources, profit)
        # print(resources)


coffee_machine(resources, profit)