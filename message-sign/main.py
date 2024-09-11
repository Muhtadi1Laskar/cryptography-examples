from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric.utils import encode_dss_signature, decode_dss_signature
from cryptography.hazmat.primitives import serialization

def generate_key_pair():
    # Generate private key using elliptic curve cryptography
    private_key = ec.generate_private_key(ec.SECP256R1())
    
    # Derive the public key from the private key
    public_key = private_key.public_key()

    return private_key, public_key

def sign_message(message, private_key):
    # Sign the message using the private key
    signature = private_key.sign(message, ec.ECDSA(hashes.SHA256()))
    return signature

def verify_signature(message, signature, public_key):
    try:
        # Verify the signature using the public key
        public_key.verify(signature, message, ec.ECDSA(hashes.SHA256()))
        return True
    except Exception:
        return False

if __name__ == "__main__":
    message = b"Hello World"

    private_key, public_key = generate_key_pair()

    signature = sign_message(message, private_key)

    is_valid = verify_signature(message, signature, public_key)

    print(f"Signature valid: {is_valid}")
