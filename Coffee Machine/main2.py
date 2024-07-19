from dicts import MENU , resources
from arts import logo , cost
profit = 0

def make_coffee(drink_name,order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕. Enjoy! ")

def is_transaction_successful(amount_received,drink_cost):
    if amount_received >= drink_cost:
        
        change = round(amount_received - drink_cost,2)
        print(f"Here is Rs {change} in change")
        global profit 
        profit += drink_cost
        
        return True
    else:
        print("Sorry! That's not enough money. Money refunded")
        return False
    

def is_resource_sufficient(oder_ingredients):
    for item in oder_ingredients:
        if oder_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True


is_on = True


print(logo,'\n')
        
print(cost,'\n')


while is_on :
    
    user_choice = input("What would you like?(espresso/latte/cappuccino): ").lower()
    
    if user_choice == "off":
        print("Thank You!")
        is_on = False
    
    elif user_choice == "report":
        print(f"""
              Water : {resources['water']} ml
              Milk : {resources['milk']} ml
              Coffee : {resources['coffee']} g
              Money : Rs {profit}
              """)
    else:
        drink = MENU[user_choice]
        if is_resource_sufficient(drink['ingredients']):
            payment = int(input("Please insert money here... : Rs "))
            if is_transaction_successful(payment,drink['cost']):
                    make_coffee(user_choice,drink['ingredients'])