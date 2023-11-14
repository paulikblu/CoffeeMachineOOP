from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

machine = CoffeeMaker()
money = MoneyMachine()
menu = Menu()
# item = MenuItem()

working = True


while working:
    options = menu.get_items()
    order = input(f"What would you like? ({options}):")
    if order == "off":
        working = False
    elif order == "report":
        machine.report()
        money.report()
    else:
        drink = menu.find_drink(order)
        if machine.is_resource_sufficient(drink):
            if money.make_payment(drink.cost):
                machine.make_coffee(drink)
