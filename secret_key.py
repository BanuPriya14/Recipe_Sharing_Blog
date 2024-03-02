import os

# Generate a secure secret key
secret_key = os.urandom(24)
secret_key_value=print(secret_key.hex())