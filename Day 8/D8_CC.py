#Caesar Cipher
from turtle import pos


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(text, shift):
    
    encrypted = ""
    for i in text:
        position = alphabet.index(i) 
        new_position = position + shift
        new_letter = alphabet[new_position]
        encrypted += new_letter
    
    print(f"The encoded text is {encrypted}")
    
def decode(text, shift):
    
    deencrypted = ""
    for i in text:
        position = alphabet.index(i) 
        new_position = position - shift
        new_letter = alphabet[new_position]
        deencrypted += new_letter
    
    print(f"The decoded text is {deencrypted}")
    

if direction == 'encrypy':
    encrypt(text, shift)
elif direction == 'decode':
    decode(text, shift)
else:
    print("ERROR")