
# Importing modules

import random
 

from hangman_words import words

from hangman_stages import stages,logo

print(logo)

choice = random.choice(words)
new_choice = list(choice)

print("Pssst, he solution is",choice)

display=[]

for i in range(len(choice)):
    display += "_"
    
print(display)
lives = 6
Found = False
while not Found:
    guess = input("Guess a number:").lower()
    
    if guess in display:
      print("You have already guessed",guess)
    
    for i in range(0,len(choice)):
        letter = choice[i]
        if letter == guess:
            display[i] = letter
            
    if guess not in choice:
      print(f"You guessed {guess}, that is not in the word. You lose a live")
      lives -= 1
      if lives == 0:
        Found = True
        print("You lose!")
      print(' '.join(display))
    
    if '_' not in display:
        Found = True
        print("You win!")
        
    print(stages[lives])

