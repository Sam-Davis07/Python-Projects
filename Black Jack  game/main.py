from arts import logo
import random

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    ran_card = random.choice(cards)
    return ran_card
    
def calculate_score(cards):
    
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)


def compare(user_score,computer_score):
    if user_score == computer_score :
        
        return "Draw 🙃"
    
    elif computer_score == 0:
    
        return "Lose, computer has Blackjack 😱"
    
    elif user_score == 0:
      
        return "Win with a Blackjack 😎"
    
    elif user_score > 21 :
    
        return "You went over. You lose 😭"
    
    elif computer_score > 21 :
    
        return "Computer went over. You win 😊"
    
    elif user_score > computer_score :
    
        return "You win 😊"
    
    else:
        
        return "You Lose 😤"    
    
        
def play_games():
    
    print(logo)
    
    user_cards = []
    computer_cards = []
    
    is_game_over = False

    for i in range(2):
        
        user_cards.append(deal_card())
        computer_cards.append(deal_card())    

    while not is_game_over:
        
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"user cards: {user_cards}  current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")


        if user_score == 0 or computer_score == 0 or user_score > 21:
        
            is_game_over = True

        else:
            print('\n')
        
            draw_card = input("draw card type 'yes' or 'no': ").lower()
        
            print('\n')
            if draw_card == "yes": 
                user_cards.append(deal_card())
        
            else:
                is_game_over = True
                
    while computer_score != 0 and  computer_score < 17:
        
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.


    print(f"    Your final hand: {user_cards}, final score: {user_score}")
    print(f"    Computer's final hand: {computer_cards}, final score: {computer_score}")
    print('\n')

    print(compare(user_score,computer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n':") == "y":
    print('\n')
    play_games()

