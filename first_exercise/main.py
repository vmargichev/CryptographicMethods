class CryptoGraphy:

    def convert_string_to_bytes_utf8(input_string):
        return input_string.encode('utf-8')

    def convert_bytes_to_string_utf8(input_byte_array):
        return input_byte_array.decode('utf-8')





byte_array = CryptoGraphy.convert_string_to_bytes_utf8('Упражнение 1 по КМЗИ')
print(byte_array)
string_output = CryptoGraphy.convert_bytes_to_string_utf8(byte_array)
print(string_output)