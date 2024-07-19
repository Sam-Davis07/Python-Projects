
import random
from Password_lns import letter, symbols, numbers

password = ""

letter_random = random.randint(1,52)

number_random = random.randint(1,9)

symbol_random = random.randint(1,10)

letter_num = int(input("How many letters do you want?\n"))

num_num = int(input('How many number do you want?\n'))

symbol_num = int(input('How many symbols do you want?\n'))

#Easy Level

for i in range(1,letter_num+1):
    new_letter = random.randint(0,51)
    password += letter[new_letter]
    
for i in range(1,num_num+1):
    NEW_NUM = random.randint(1,9)
    password += str(numbers[NEW_NUM])
    
for i in range(1,symbol_num+1):
    new_symbol = random.randint(1,10)
    password += symbols[new_symbol]
print(password)

#Hard Level

password_list = []

for i in range(1,letter_num+1):
    new_letter = random.randint(0,51)
    password_list.append(letter[new_letter])

for i in range(1,num_num+1):
    password_list += str(random.choice(numbers))
    
for i in range(1,symbol_num+1):
    password_list += random.choice(symbols)    
x = random.shuffle(password_list)

password = ""

for i in password_list:
    password += i

print(password)

    