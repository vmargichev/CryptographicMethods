import hashlib
import sys

FILE_PATH = "new_file.txt"

input = input("Insert").encode("utf-8")
hash_md5 = hashlib.md5()
hash_sha_256 = hashlib.sha256()
hash_sha_512 = hashlib.sha512()

hash_md5.update(input)
hash_sha_256.update(input)
hash_sha_512.update(input)

# print(input)
# print(hash_md5.digest())
# print(hash_sha_256.digest())
# print(hash_sha_512.digest())
file1 = open(FILE_PATH, "w+")
file1.write(hash_md5.hexdigest() + '\n')
file1.write(hash_sha_256.hexdigest() + '\n')
file1.write(hash_sha_512.hexdigest() + '\n')

file1.close()


