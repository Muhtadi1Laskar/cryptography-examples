import os
import ecdsa
import hashlib
import base58

def generate_private_key():
    return os.urandom(32)

def private_key_to_public_key(private_key):
    sk = ecdsa.SigningKey.from_string(private_key, curve=ecdsa.SECP256k1)
    vk = sk.verifying_key

    return b'\x04' + vk.to_string()

def public_key_to_address(public_key):
    sha256_bpk = hashlib.sha256(public_key).digest()
    ripemd160_bpk = hashlib.new('ripemd160', sha256_bpk).digest()
    hashed_pubkey = b'\x00' + ripemd160_bpk
    checksum = hashlib.sha256(hashlib.sha256(hashed_pubkey).digest()).digest()[:4]
    binary_address = hashed_pubkey + checksum

    return base58.b58encode(binary_address)

# Main code to generate a Bitcoin address from a private key
private_key = generate_private_key()
print(f"Private Key (hex): {private_key.hex()}")

public_key = private_key_to_public_key(private_key)
print(f"Public Key (hex): {public_key.hex()}")

bitcoin_address = public_key_to_address(public_key)
print(f"Bitcoin Address: {bitcoin_address.decode()}")