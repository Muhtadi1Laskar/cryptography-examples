import hashlib
import json

def read_file():
    with open("data.txt", "r") as f:
        return f.read()

def hash_function(message, type):
    hash_func = hashlib.new(type)
    encoded_str = bytes(message, encoding='utf-8')

    hash_func.update(encoded_str)

    if type == 'shake_256' or type == 'shake_128':
        return hash_func.hexdigest(20)

    return hash_func.hexdigest()


if __name__ == '__main__':
    message = read_file()
    hash_data = hash_function(message, 'sha256')

    print(hash_data)