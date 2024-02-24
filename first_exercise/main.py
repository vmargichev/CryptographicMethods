class CryptoGraphy:
    def read_from_file(file_path):
        with open(file_path, 'r') as file:
            return file.read().rstrip()
        
    def save_to_file(string_input):
        with open('file_new.txt', 'w') as file:
            file.write(string_input)
        return None


    def convert_string_to_bytes_utf8(input_string):
        return input_string.encode('utf-8')

    def convert_bytes_to_string_utf8(input_byte_array):
        return input_byte_array.decode('utf-8')




# first_exercise/file.txt
byte_array = CryptoGraphy.convert_string_to_bytes_utf8(CryptoGraphy.read_from_file('/home/margichev/workspace/github.com/username/CryptographicMethods/first_exercise/file.txt'))
print(byte_array)
string_output = CryptoGraphy.convert_bytes_to_string_utf8(byte_array)
print(string_output)
CryptoGraphy.save_to_file(string_output)