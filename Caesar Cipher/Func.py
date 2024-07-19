
from alphabets import alphabet


def encrypt(plain_text,shift_amount):
    
    cipher_text = ""
    
    for i in range(0,len(plain_text)):
        if plain_text[i] in alphabet:
            position = alphabet.index(plain_text[i])
            new_position = position + shift_amount
            cipher_text += alphabet[new_position]
        else:
            cipher_text += plain_text[i]
    print(f"The encoded text is {cipher_text}") 
    
    
def decrypt(plain_text,shift_amount):
    
    cipher_text = ""
    
    for i in range(0,len(plain_text)):
        
        position = alphabet.index(plain_text[i])
        new_position = position - shift_amount
        cipher_text += alphabet[new_position]
    
    print(f"The decoded text is {cipher_text}")
