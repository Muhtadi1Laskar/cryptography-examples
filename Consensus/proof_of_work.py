import hashlib
import time


def proof_of_work(message, difficulty):
    nonce = 0
    prefix = '0' * difficulty
    start_time = time.time()

    while True:
        text = message + str(nonce)
        block_hash = hashlib.sha256(text.encode()).hexdigest()

        if block_hash.startswith(prefix):
            end_time = time.time()
            print(f"Success with nonce: {nonce}")
            print(f"Hash: {block_hash}")
            print(f"Time Taken: {end_time - start_time} seconds")

            return nonce, block_hash
        
        nonce += 1


block_data = "Block header data here"

difficulty = 10

proof_of_work(block_data, difficulty)