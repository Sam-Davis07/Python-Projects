import random
import arts

ran_num = random.randint(1,100)


def Check(lives):
    
    while lives >= 0 :
    
        user_guess = int(input("Make a Guess: "))
        lives -= 1
    
        if user_guess > ran_num :
    
            print("Too High...\n")
            print(f"You have {lives} lives left to guess the number.")
            print("\n")
        
        elif user_guess < ran_num :
    
            print("Too Low...\n")
            print(f"You have {lives} lives left to guess the number.")
            print("\n")
            
        elif user_guess == ran_num :
    
            print(arts.win,"\n")
            print(f"The correct answer is : {ran_num}\n")
            break
        
        if lives == 0 :
    
            print(arts.lost,'\n')
            print("Lives left :",lives,"\n")
            print("Answer is :",ran_num,'\n')
            break
        
print(arts.logo,"\n")

print("Welcome to the Number Guessing Game!\n")

print("I'm thinking of a number between 1 and 100.\n")

ch = input("Choose a difficulty. Type 'easy' or 'hard':").lower()

if ch == "easy" :
    
    print("You have 10 attempts to guess the number.")
    Check(10)

elif ch == "hard" :
    
    Check(5)

else:
    
    print("Please enter a valis input...")