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
    "water": 1000,
    "milk": 2000,
    "coffee":40,
}

def resource_check(order_ingredients):
   for item in order_ingredients:
      if order_ingredients[item] > resources[item]:
         print(f"Resource {item} is not sufficient")
         return False
   return True
         
   
def make_coffee(order_ingredients):
   for item in order_ingredients:
      resources[item] -= order_ingredients[item]



def process_coins():
  total = 0 
  print("Enter Coins \n")
  total += float(input("Enter no. of quarters: ")) * 0.25
  total += float(input("Enter no. of dimes: ")) * 0.10
  total += float(input("Enter no. of nickles: ")) * 0.05
  total += float(input("Enter no. of pennies: ")) * 0.01
  return total

def check_transaction(coffee_cost, payment_info):
   if payment_info >= coffee_cost:
      change = round((payment_info - coffee_cost),2)
      print(f"\nYou've paid extra please collect your change ${change}")
      global profit 
      profit += coffee_cost
      return True
   else:
      print("Sorry not enough money!!")
      return False

ON = True

while ON:
    choice = input("What you like to have: \n 1. Espresso \n 2. Latte \n 3. Cappuccino \n").lower()
    if choice == "off":
        print("Secret Shutdown initiated, Maching turning off!")
        ON = False
    elif choice == "report":
        print(f"Current Report of Available Resource:")
        print(f"Water : {resources['water']}")
        print(f"Milk : {resources['milk']}")
        print(f"Coffee: {resources['coffee']}")
        print(f"Profit Earned: {round(profit)}")
    else:
        coffee = MENU[choice]
        order_ingredients = coffee["ingredients"]
        coffee_cost = coffee["cost"]
        if resource_check(order_ingredients):
            payment_info = process_coins()
            if check_transaction(coffee_cost, payment_info):
                print("")
                print(f"{choice} is getting prepared")
                make_coffee(order_ingredients)
                print(resources)
                print(f"Here you go, Enjoy your {choice}")
        else:
            exit()
