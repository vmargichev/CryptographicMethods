def caesar_cipher(message, shift):
    alphabet = " АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЬЮЯ"
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    table = str.maketrans(alphabet, shifted_alphabet)
    return message.translate(table)

message = "НИЕ СМЕ СТУДЕНТИ ОТ ТУ СОФИЯ"
shift = 1
encrypted_message = caesar_cipher(message, shift)
print(encrypted_message)
