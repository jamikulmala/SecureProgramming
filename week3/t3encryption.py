# File encrypter and decrypter using AES-256

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import secrets

def generate_key():
    # Generate a random 256-bit key
    return secrets.token_bytes(32)

def encrypt_file(input_file, output_file, key):
    with open(input_file, 'rb') as f:
        plaintext = f.read()

    # Generate a random 128-bit Vector
    v = secrets.token_bytes(16)

    # Create an AES-256 Cipher object
    cipher = Cipher(algorithms.AES(key), modes.CFB(v), backend=default_backend())

    # Encrypt the plaintext
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(plaintext) + encryptor.finalize()

    # Write the IV and ciphertext to the output file
    with open(output_file, 'wb') as f:
        f.write(v)
        f.write(ciphertext)

def decrypt_file(input_file, output_file, key):
    with open(input_file, 'rb') as f:
        # Read the IV from the file
        v = f.read(16)
        ciphertext = f.read()

    # Create an AES-256 Cipher object
    cipher = Cipher(algorithms.AES(key), modes.CFB(v), backend=default_backend())

    # Decrypt the ciphertext
    decryptor = cipher.decryptor()
    plaintext = decryptor.update(ciphertext) + decryptor.finalize()

    # Write the decrypted plaintext to the output file
    with open(output_file, 'wb') as f:
        f.write(plaintext)

if __name__ == "__main__":

    # Example usage
    input_file = "user_credentials.csv"
    encrypted_file = "encrypted_file.bin"
    decrypted_file = "decrypted_file.txt"

    # Secret key
    key = generate_key()

    # Encrypt the file
    encrypt_file(input_file, encrypted_file, key)

    # Decrypt the file
    decrypt_file(encrypted_file, decrypted_file, key)