import hashlib

def hash_function(message, type):
    hash_func = hashlib.new(type)
    encoded_str = bytes(message, encoding='utf-8')

    hash_func.update(encoded_str)

    if type == 'shake_256' or type == 'shake_128':
        return hash_func.hexdigest(20)

    return hash_func.hexdigest()


if __name__ == '__main__':
    message = 'This is a message'
    hash_data = hash_function(message, 'sha256')

    print(hash_data)