print("Welcome to Ceaser Cipher Encryption! ")

# alphabet_list = [chr(letter) for letter in range(ord('a'), ord('z') + 1)]
alphabet_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
                 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount += -1
    for char in start_text:
        if char in alphabet_list:
            position = alphabet_list.index(char)
            new_position = position + shift_amount
            new_letter = alphabet_list[new_position]
            end_text += new_letter
        else:
            end_text += char
    print(f"The {cipher_direction} text is: {end_text}")


while True:
    direction = input("Type 'encode' to encrypt, or 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26

    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

    restart = input("'Yes' to restart, 'No' to quit.\n").lower()
    if restart == "no":
        print("Goodbye")
        break

