import random

def simple_hash(message):
    hash_value = 0

    for elem in message:
        hash_value += ord(elem)
    
    return hash_value


if __name__ == '__main__':
    data = 'This is a string'
    hash_value = simple_hash(data)

    print(hash_value)
    