def trithemius_cipher(message, key):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    encrypted_message = ""
    key_length = len(key)
    
    for i in range(len(message)):
        if message[i] == " ":
            encrypted_message += " "
        else:
            shift = (alphabet.index(key[i % key_length]) + 1) % 26
            new_index = (alphabet.index(message[i]) + shift) % 26
            encrypted_message += alphabet[new_index]
    
    return encrypted_message

message = "SETSRELATIONSANDFUNCTIONS"
key = "COVER"
encrypted_message = trithemius_cipher(message, key)
print(encrypted_message)
