from arts import logo , cost

from dicts import MENU , resources

profit = 0

def cost_item(user_choice,amount_received):
    cost_item = MENU[user_choice]["cost"]
    if cost_item > amount_received :
        change = cost_item - amount_received
        print(f"Here is Rs {change} in change.")
        print(f"Here is your {user_choice} ☕. Enjoy!\n")

def details_of_user_choice(user_choice):
    
    total_water = resources["water"]
    
    total_milk = resources["milk"]
    
    total_coffee = resources["coffee"]
    
    if user_choice == "report":
        print(f"""
              Water : {total_water} ml
              Milk : {total_milk} ml
              Coffee : {total_coffee} g
              """)
    
    elif user_choice == "latte":
        amount_recevied = int(input("\nPlease insert money here: Rs "))
        total_water -= MENU[user_choice]['ingredients']['water']
        total_coffee -= MENU[user_choice]['ingredients']["coffee"]
        total_milk -= MENU[user_choice]['ingredients']["milk"]
        cost_item(user_choice,amount_recevied)
        
    elif user_choice == "cappuccino":
        amount_recevied = int(input("\nPlease insert money here: Rs "))
        total_water -= MENU[user_choice]['ingredients']['water']
        total_coffee -= MENU[user_choice]['ingredients']["coffee"]
        total_milk -= MENU[user_choice]['ingredients']["milk"]
        cost_item(user_choice,amount_recevied)
    
    elif user_choice == "espresso":
        amount_recevied = int(input("\nPlease insert money here: Rs "))
        total_water = MENU[user_choice]['ingredients']['water']
        total_coffee -= MENU[user_choice]['ingredients']["coffee"]
        cost_item(user_choice,amount_recevied)
    
print(logo,'\n')

print(cost)
while True:
    user_choice = input("What would you like?(espresso/latte/cappuccino): ").lower()
    

    details_of_user_choice(user_choice)


# print(MENU["espresso"]["ingredients"])

