from alphabets import logo

from Func import encrypt, decrypt
 
def caesar(direction,text,shift):
    
    if direction == "encode":
    
        encrypt(text,shift)
    
    elif direction == "decode":
    
        decrypt(text,shift)
    
    else:
    
        print("Please enter a valid input!")
        
        

print(logo)

ans = "yes"

while ans == "yes":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()

    text = input("Type your message:\n").lower()

    if " " in text :
        print("Don't put any whitespaces...\n")
        ans = input("Do you want to continue(yes/no):").lower()
        if ans != "yes":
            break
    else:
        shift = int(input("Type the shift number:\n"))

        shift = shift % 26

        caesar(direction,text,shift)
        
        ans = input("Do you want to continue(yes/no):").lower()
        if ans != "yes":
            break

