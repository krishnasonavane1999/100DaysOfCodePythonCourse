MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 40.0,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 80.0,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 100.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


logo = '''_________         _____  _____                  _____                .__    .__               
\_   ___ \  _____/ ____\/ ____\____   ____     /     \ _____    ____ |  |__ |__| ____   ____  
/    \  \/ /  _ \   __\\   __\/ __ \_/ __ \   /  \ /  \\__  \ _/ ___\|  |  \|  |/    \_/ __ \ 
\     \___(  <_> )  |   |  | \  ___/\  ___/  /    Y    \/ __ \\  \___|   Y  \  |   |  \  ___/ 
 \______  /\____/|__|   |__|  \___  >\___  > \____|__  (____  /\___  >___|  /__|___|  /\___  >
        \/                        \/     \/          \/     \/     \/     \/        \/     \/ '''
        
print(logo)
def process_coins():

  one_rupee_coins = int(input("How many coins of 1₹: )"))
  two_rupee_coins = int(input("How many coins of 2₹: )"))
  five_rupee_coins = int(input("How many coins of 5₹: )"))
  ten_rupee_coins = int(input("How many coins of 10₹: )"))

  total_by_user = (one_rupee_coins) + (2 * two_rupee_coins) + (5 * five_rupee_coins) + (10 * ten_rupee_coins)

  return total_by_user;

def check_for_resources_availability(user_choice):
  
  if user_choice == "espresso":
    required_water = MENU["espresso"]["ingredients"]["water"]
    required_coffee = MENU["espresso"]["ingredients"]["coffee"]

    available_water = resources["water"]
    available_coffee = resources["coffee"]
    
    if available_water >= required_water and available_coffee >= required_coffee:
            resources["water"] -= required_water
            resources["coffee"] -= required_coffee

            return True
    else:
      return False

  elif user_choice == "latte":
        required_water = MENU["latte"]["ingredients"]["water"]
        required_milk = MENU["latte"]["ingredients"]["milk"]
        required_coffee= MENU["latte"]["ingredients"]["coffee"]

        available_water = resources["water"]
        available_milk = resources["milk"]
        available_coffee = resources["coffee"]

        if available_water >= required_water and available_coffee >= required_coffee and available_milk >= required_milk:
                resources["water"] -= required_water
                resources["milk"] -= required_milk
                resources["coffee"] -= required_coffee

                return True
        else:
          return False

  elif user_choice == "cappuccino":
        required_water = MENU["cappuccino"]["ingredients"]["water"]
        required_milk = MENU["cappuccino"]["ingredients"]["milk"]
        required_coffee= MENU["cappuccino"]["ingredients"]["coffee"]

        available_water = resources["water"]
        available_milk = resources["milk"]
        available_coffee = resources["coffee"]

        if available_water >= required_water and available_coffee >= required_coffee and available_milk >= required_milk:
          resources["water"] -= required_water
          resources["milk"] -= required_milk
          resources["coffee"] -= required_coffee

          return True
        else:
          return False

  else:
    return False


def give_overall_report():
  for content in resources:
    print(f"{content}: {resources[content]}")


def check_for_money_sufficiency(user_choice, money_from_user):
    if user_choice == 'espresso':
        bill_amount = MENU[user_choice]["cost"]
        
        if money_from_user < bill_amount:
            return "not sufficient"
        else:
          return money_from_user - bill_amount 

    elif user_choice == 'latte':
      bill_amount = MENU[user_choice]["cost"]
        
      if money_from_user < bill_amount:
          return "not sufficient"
      else:
        return money_from_user - bill_amount 

    elif user_choice == 'cappuccino':
      bill_amount = MENU[user_choice]["cost"]
        
      if money_from_user < bill_amount:
          return "not sufficient"
      else:
        return money_from_user - bill_amount 


cafe_open = 'y'
while cafe_open == 'y':
  def process_order():
    user_choice = input("What you would like? (espresso/latte/cappuccino) ")

    if user_choice == "report":
        give_overall_report()
    elif user_choice == "espresso":
        are_resources_available = check_for_resources_availability(user_choice)
        if are_resources_available:
              money_from_user = process_coins()
              is_amount_sufficient = check_for_money_sufficiency(user_choice, money_from_user)
              if is_amount_sufficient != "not sufficient":
                      print(f"Here is your order!!☕ and Your change {is_amount_sufficient}")
              else:
                      print("Sorry, we can not process this order. Please check your payment amount again")

        else:
          print("Sorry, resources are not available to ake your order.")


    elif user_choice == "latte":
      are_resources_available = check_for_resources_availability(user_choice)
      if are_resources_available:
          money_from_user = process_coins()
              
          is_amount_sufficient = check_for_money_sufficiency(user_choice, money_from_user)
          if is_amount_sufficient != "not sufficient":
                      print(f"Here is your order!!☕ and Your change {is_amount_sufficient}")
          else:
                      print("Sorry, we can not process this order. Please check your payment amount again")

      else:
        print("Sorry, resources are not available to ake your order.")
    elif user_choice == "cappuccino":
      are_resources_available = check_for_resources_availability(user_choice)
      if are_resources_available:
              money_from_user = process_coins()
              
              is_amount_sufficient = check_for_money_sufficiency(user_choice, money_from_user)
              if is_amount_sufficient != "not sufficient":
                      print(f"Here is your order!!☕ and Your change {is_amount_sufficient}")
              else:
                      print("Sorry, we can not process this order. Please check your payment amount again")
      else:
        print("Sorry, resources are not available to ake your order.")

    else:
      print("Sorry we don't have what you ordered at this time.")

  if cafe_open == 'y':
    process_order()
    cafe_open = 'y'
  else:
    print("Have a nice day, Visit Again!!")
    cafe_open = 'n'

  cafe_open = input("Want to order something else? 'y' or 'n'? ")
