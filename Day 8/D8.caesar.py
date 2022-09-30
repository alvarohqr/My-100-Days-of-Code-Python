#Caesar Cipher


from types import CellType


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def Caesar(direction, text, shift):
    new_text = ''
    if direction == 'decode':
        shift *= -1
                
    for i in text:
        position = alphabet.index(i) 
        new_position = position + shift
        new_letter = alphabet[new_position]
        new_text += new_letter
        
    print(f"The {direction}d text is {new_text}")
     
    

Caesar(direction, text, shift)
