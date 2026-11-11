alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(original_text, shift_amount, encode_or_decode):
    cipher_text = ""
    if encode_or_decode == 'decode':
        shift_amount *= -1
    for letter in original_text:
        if letter not in alphabet:
            cipher_text += letter
        else:
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)
            cipher_text += alphabet[shifted_position]
    print(f"Here is the {encode_or_decode}d result: {cipher_text}")


repeat = True
while repeat == True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()

    while direction != 'decode' and direction != 'encode':
        print("Invalid Direccion!")
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    else:
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)
        repeat = input("Type ´yes' or 'no':\n").lower()
        if repeat == 'no':
            repeat = False
            print("Goodbye")
        else:
            repeat = True
