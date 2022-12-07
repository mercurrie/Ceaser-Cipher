from art import logo
print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
            'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 
            'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 
            't', 'u', 'v', 'w', 'x', 'y', 'z']

def ceaser(message, position, crypt):
    newMsg = ""
    if crypt == 'decode':
        position *= -1

    for char in message:
        if char in alphabet:
            i = (alphabet.index(char) + position)
            newMsg += alphabet[i] 
        else:
            newMsg += char
            
        
    print(f'The {crypt}d text is: {newMsg}')


again = True
while again:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    # % to prevent user from entering amount out of bounds o f list
    shift = int(input("Type the shift number:\n")) % 26
    
    ceaser(message = text, position = shift, crypt = direction)
    answer = input("Would you like to 'Encode' or 'Decode another message? Type yes or no ")
    
    if answer == "yes":
        again = True
    else:
        again = False