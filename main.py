from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine 

coffee_machine = CoffeeMaker()
coffee_name = Menu()
payments = MoneyMachine()
ON = True

while ON:
    drink = input(f"What would like:\n{coffee_name.get_items()}\n").lower()
    if drink == "report":
        print(coffee_machine.report())
        print(payments.report())
    elif drink == "off":
        print("Shutting Down!!\n")
        ON = False
    else:
        selected_drink = coffee_name.find_drink(drink) 
        if coffee_machine.is_resource_sufficient(selected_drink):
          if payments.make_payment(selected_drink.cost):
             coffee_machine.make_coffee(selected_drink)
        



