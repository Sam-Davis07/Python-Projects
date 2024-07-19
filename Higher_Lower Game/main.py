import random
from art import logo , vs
from game_data import data 



def printing_details_A():    
        
    ran_num = random.randint(0,len(data)-1)
    print(logo,'\n')
    print(f"Compare A: {data[ran_num]['name']}, {data[ran_num]['description']}, {data[ran_num]['country']},\n")
    return data[ran_num]['follower_count']

def printing_details_B():
        
    ran_num = random.randint(0,len(data))
    print(vs,'\n')
    print(f"Compare B: {data[ran_num]['name']}, {data[ran_num]['description']}, {data[ran_num]['country']}.\n")
    return data[ran_num]['follower_count']


def Check(a,b):
    global score 
    ch = input("Who has more followers? Type 'A' or 'B': ").upper()

    if ch == 'A':
        if a > b:
            score += 1
            print("Correct, Final Score ",score)
        else:
            print("Wrong!")
    elif ch == 'B':
        if b > a :
            print("You are Correct!",score)
            score +=1 
        else:
            print("Wrong")
            
    else:
        print("You are wrong! , Final score",score)

score = 0

while score >= 0 :    
    a = printing_details_A()
    b = printing_details_B()
    sc = Check(a,b)
    
    
    


